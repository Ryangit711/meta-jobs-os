#!/bin/bash
# CADENCE CTL — Update networking cadence from user commands
# Usage: bash scripts/cadence_ctl.sh [command] [args...]
#
# Commands:
#   submit [company]          — Record submission date, start T+0
#   update [company] [leg] [status] — Mark leg as sent/replied/complete
#   contact [company] [name] [title] [linkedin_url] — Add contact
#   show                     — Show full tracker
#   footer                   — Show footer only

CADENCE_FILE="/home/aryan/opencode_test/ABHIMANYU-2.0/data/networking/cadence.json"
TRACKER_FILE="/home/aryan/opencode_test/ABHIMANYU-2.0/data/networking/NETWORKING_TRACKER.md"
FOOTER_FILE="/home/aryan/opencode_test/ABHIMANYU-2.0/data/networking/CADENCE_FOOTER.md"

cmd=$1
shift

case "$cmd" in
    submit)
        company="$*"
        python3 -c "
import json, datetime
today = datetime.date.today().isoformat()
with open('$CADENCE_FILE', 'r') as f:
    data = json.load(f)
for c in data['companies']:
    if c['company'].lower() == '$company'.lower():
        c['status'] = 'submitted'
        c['submit_date'] = today
        # Set T+0 legs
        for leg_num in ['1','2','3','4','5']:
            if leg_num in c['legs']:
                due = datetime.date.today() + datetime.timedelta(days={1:0,2:3,3:7,4:14,5:28}[int(leg_num)])
                c['legs'][leg_num]['due'] = due.isoformat()
                c['legs'][leg_num]['status'] = 'due_today' if leg_num == '1' else 'future'
        c['legs']['1']['status'] = 'due_today'
        print(f\"✅ Submitted: {c['company']} — T+0 timer started. Leg 1 (Connect) due today.\")
        break
else:
    print(f\"❌ Company not found: $company\")
    exit(1)
with open('$CADENCE_FILE', 'w') as f:
    json.dump(data, f, indent=2)
" && bash /home/aryan/opencode_test/ABHIMANYU-2.0/scripts/update_cadence.sh > /dev/null 2>&1
        ;;
    
    update)
        company="$1"; leg="$2"; status="$3"
        python3 -c "
import json
with open('$CADENCE_FILE', 'r') as f:
    data = json.load(f)
for c in data['companies']:
    if c['company'].lower() == '$company'.lower():
        if '$leg' in c['legs']:
            c['legs']['$leg']['status'] = '$status'
            print(f\"✅ Updated {c['company']} Leg $leg → $status\")
        else:
            print(f\"❌ Leg $leg not found\")
            exit(1)
        break
else:
    print(f\"❌ Company not found: $company\")
    exit(1)
with open('$CADENCE_FILE', 'w') as f:
    json.dump(data, f, indent=2)
" && bash /home/aryan/opencode_test/ABHIMANYU-2.0/scripts/update_cadence.sh > /dev/null 2>&1
        ;;
    
    contact)
        company="$1"; name="$2"; title="$3"; linkedin="$4"
        python3 -c "
import json
with open('$CADENCE_FILE', 'r') as f:
    data = json.load(f)
for c in data['companies']:
    if c['company'].lower() == '$company'.lower():
        c['contacts'].append({
            'name': '$name',
            'title': '$title',
            'linkedin': '$linkedin',
            'leg_assigned': len(c['contacts']) + 1
        })
        print(f\"✅ Added contact: {name} — {title}\")
        break
else:
    print(f\"❌ Company not found: $company\")
    exit(1)
with open('$CADENCE_FILE', 'w') as f:
    json.dump(data, f, indent=2)
" && bash /home/aryan/opencode_test/ABHIMANYU-2.0/scripts/update_cadence.sh > /dev/null 2>&1
        ;;
    
    show)
        cat "$TRACKER_FILE"
        ;;
    
    footer)
        cat "$FOOTER_FILE"
        ;;
    
    *)
        echo "Usage: $0 {submit|update|contact|show|footer} [args...]"
        echo ""
        echo "  submit [company]              — Record submission, start timer"
        echo "  update [company] [leg] [status] — Mark: sent/replied/complete/skipped"
        echo "  contact [company] [name] [title] [url] — Add networking contact"
        echo "  show                          — Full NETWORKING_TRACKER.md"
        echo "  footer                        — Live CADENCE_FOOTER.md"
        ;;
esac
