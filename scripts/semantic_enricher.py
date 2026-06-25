#!/usr/bin/env python3
"""
Semantic Enricher — Generates schema.org JSON-LD from SHOOT package data.
Attached alongside DOCX for next-gen ATS platforms (Workday Skills Cloud, etc.).

Usage:
  python3 scripts/semantic_enricher.py --data shoot_data.json
  python3 scripts/semantic_enricher.py --company Deloitte --role "Sr Mgr" --skills strategic,operations
"""

import argparse
import json
import sys


def build_jsonld(company, role, name="[NAME]", skills=None, experience=None,
                 education=None, location="Vancouver, BC, Canada",
                 phone="[PHONE]", email="[EMAIL]", linkedin="[LINKEDIN]"):
    skills = skills or []
    experience = experience or []
    education = education or []

    person = {
        "@context": "http://schema.org",
        "@type": "Person",
        "name": name,
        "telephone": phone,
        "email": email,
        "sameAs": [linkedin],
        "jobTitle": role,
        "worksFor": {
            "@type": "Organization",
            "name": company
        },
        "location": {
            "@type": "Place",
            "name": location
        },
        "knowsAbout": []
    }

    for skill in skills:
        skill_entry = {
            "@type": "DefinedTerm",
            "name": skill
        }
        person["knowsAbout"].append(skill_entry)

    if experience:
        person["hasOccupation"] = []
        for exp in experience:
            occ = {
                "@type": "Occupation",
                "name": exp.get("title", ""),
                "employer": {
                    "@type": "Organization",
                    "name": exp.get("company", "")
                }
            }
            if "start_date" in exp:
                occ["startDate"] = exp["start_date"]
            if "end_date" in exp:
                occ["endDate"] = exp["end_date"]
            if "description" in exp:
                occ["description"] = exp["description"]
            person["hasOccupation"].append(occ)

    if education:
        person["alumniOf"] = []
        for edu in education:
            inst = {
                "@type": "EducationalOrganization",
                "name": edu.get("institution", "")
            }
            if "degree" in edu:
                inst["description"] = edu["degree"]
            if "field" in edu:
                inst["description"] = inst.get("description", "") + f" - {edu['field']}"
            person["alumniOf"].append(inst)

    return person


def main():
    parser = argparse.ArgumentParser(description='Generate schema.org JSON-LD for resume enrichment')
    parser.add_argument('--data', help='JSON file with structured resume data')
    parser.add_argument('--company', default='[Company]', help='Target company name')
    parser.add_argument('--role', default='[Role]', help='Target role title')
    parser.add_argument('--name', default='[NAME]', help='Candidate name')
    parser.add_argument('--skills', default='', help='Comma-separated skill list')
    parser.add_argument('--location', default='Vancouver, BC, Canada', help='Location')
    parser.add_argument('--pretty', action='store_true', help='Pretty-print JSON output')
    parser.add_argument('--output', help='Write to file instead of stdout')
    args = parser.parse_args()

    if args.data:
        with open(args.data) as f:
            data = json.load(f)
    else:
        data = {
            "company": args.company,
            "role": args.role,
            "name": args.name,
            "skills": [s.strip() for s in args.skills.split(',') if s.strip()],
            "location": args.location,
            "experience": [],
            "education": []
        }

    jd = build_jsonld(
        company=data.get("company", args.company),
        role=data.get("role", args.role),
        name=data.get("name", args.name),
        skills=data.get("skills", []),
        experience=data.get("experience", []),
        education=data.get("education", []),
        location=data.get("location", args.location)
    )

    indent = 2 if args.pretty else None
    output = json.dumps(jd, indent=indent)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"Written to {args.output}")
    else:
        print(output)


if __name__ == '__main__':
    main()
