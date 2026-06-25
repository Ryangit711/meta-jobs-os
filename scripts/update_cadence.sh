#!/bin/bash
# NETWORKING CADENCE UPDATER — Run hourly via DAEMON
# Updates T+ days, leg status, generates footer
# Usage: bash scripts/update_cadence.sh

CADENCE_FILE="/home/aryan/opencode_test/ABHIMANYU-2.0/data/networking/cadence.json"
TRACKER_FILE="/home/aryan/opencode_test/ABHIMANYU-2.0/data/networking/NETWORKING_TRACKER.md"
FOOTER_FILE="/home/aryan/opencode_test/ABHIMANYU-2.0/data/networking/CADENCE_FOOTER.md"
DAEMON_LOG="/home/aryan/opencode_test/ABHIMANYU-2.0/data/daemon/daemon.log"

TODAY=$(date '+%Y-%m-%d')
TODAY_TS=$(date -d "$TODAY" +%s)

# Read cadence JSON — use python for robust parsing
python3 -c "
import json, datetime, sys

today = datetime.date.today()
today_str = today.isoformat()

with open('$CADENCE_FILE', 'r') as f:
    data = json.load(f)

footer_lines = []
footer_lines.append('## NETWORKING CADENCE — Live as of $TODAY')
footer_lines.append('')
footer_lines.append('| Company | Role | Stage | T+ | Leg | Due | Action |')
footer_lines.append('|---------|------|:-----:|:--:|:---:|:---:|--------|')

for company in data['companies']:
    name = company['company']
    role = company['role']
    status = company['status']
    submit_date = company['submit_date']
    
    if submit_date:
        submit_ts = datetime.date.fromisoformat(submit_date)
        t_days = (today - submit_ts).days
        
        # Map leg based on T+ days
        if t_days >= 28:
            cur_leg = 5
        elif t_days >= 14:
            cur_leg = 4
        elif t_days >= 7:
            cur_leg = 3
        elif t_days >= 3:
            cur_leg = 2
        elif t_days >= 0:
            cur_leg = 1
        else:
            cur_leg = 0
        
        company['t_plus_days'] = t_days
        company['current_leg'] = cur_leg
        
        # Update leg statuses
        for leg_num, leg_data in company['legs'].items():
            leg_num = int(leg_num)
            if leg_num == 0:
                continue
            leg_due = datetime.date.fromisoformat(leg_data['due']) if leg_data['due'] else None
            
            if leg_data['status'] in ['complete', 'sent']:
                pass  # Keep existing
            elif leg_due and leg_due < today and leg_data['status'] == 'future':
                leg_data['status'] = 'overdue'
            elif leg_due and leg_due == today and leg_data['status'] == 'future':
                leg_data['status'] = 'due_today'
            elif leg_num > cur_leg and leg_data['status'] not in ['complete', 'sent']:
                leg_data['status'] = 'future'
            elif leg_num < cur_leg and leg_data['status'] not in ['complete', 'sent']:
                pass  # Keep as-is (might be overdue)
        
        # Status icon
        if status == 'submitted':
            s_icon = '✅'
        elif status == 'shot':
            s_icon = '🔵'
        elif status == 'live':
            s_icon = '🟢'
        elif status == 'callback':
            s_icon = '📞'
        elif status == 'offer':
            s_icon = '💰'
        elif status == 'rejected':
            s_icon = '❌'
        else:
            s_icon = '🟢'
        
        # Leg icon
        if cur_leg == 0:
            leg_icon = '⏸️'
        elif cur_leg == 5:
            leg_icon = '🔴'
        else:
            leg_icon = ['⏳', '🟡', '🟠', '🔴', '🔴'][min(cur_leg-1, 4)]
        
        # Action text
        if status == 'shot' and not submit_date:
            action = 'SUBMIT APPLICATION'
        else:
            leg_actions = {1:'Connect LinkedIn', 2:'Follow-up message', 3:'Value-add touchpoint', 4:'Check-in', 5:'Close loop'}
            action = leg_actions.get(cur_leg, 'Review')
        
        # Due date
        legs = company['legs']
        due_str = str(legs.get(str(cur_leg), {}).get('due', '—')) if cur_leg > 0 else 'TODAY'
        
        footer_lines.append(f\"| {s_icon} {name} | {role[:30]} | {status.upper()} | T+{t_days} | Leg {cur_leg} {leg_icon} | {due_str} | **{action}** |\")
    else:
        # Not submitted yet
        footer_lines.append(f\"| 🔵 {name} | {role[:30]} | SHOT | — | ⏸️ | TODAY | **SUBMIT FIRST** |\")

data['last_updated'] = f\"{today_str} $(date '+%H:%M')\"

with open('$CADENCE_FILE', 'w') as f:
    json.dump(data, f, indent=2)

with open('$FOOTER_FILE', 'w') as f:
    f.write('\\n'.join(footer_lines))
    f.write('\\n')

print('Cadence updated successfully')
for line in footer_lines:
    print(line)
" 2>&1 | tee -a "$DAEMON_LOG"

# Also update the TRACKER.md with current status
python3 -c "
import json, datetime

today = datetime.date.today()

with open('$CADENCE_FILE', 'r') as f:
    data = json.load(f)

with open('$TRACKER_FILE', 'r') as f:
    tracker = f.read()

# Simple update: rewrite the timestamp
import re, subprocess
time_str = subprocess.check_output(['date', '+%H:%M']).decode().strip()
tracker = re.sub(r'Last updated:.*', f'Last updated: {today.isoformat()} {time_str} — auto-updated', tracker)

with open('$TRACKER_FILE', 'w') as f:
    f.write(tracker)
"

echo "---"
echo "TRACKER.md updated: $TRACKER_FILE"
echo "FOOTER.md generated: $FOOTER_FILE"
