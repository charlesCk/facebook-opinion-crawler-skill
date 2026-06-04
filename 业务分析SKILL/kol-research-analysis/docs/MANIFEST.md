# Manifest - KOL Research Analysis

## Included

| File | Purpose |
| --- | --- |
| `README.md` | Public-safe project positioning and reuse boundary. |
| `references/analysis-framework.md` | KOL material, authorization, acquisition, appointment, conversion, and regional comparison framework. |
| `references/public-safe-template.md` | Template for public-safe KOL review output. |

## Not Included

- Raw Feishu documents, internal meeting notes, KOL quotations, contracts, authorization details, cost tables, revenue data, or screenshots.
- Real customer, student, parent, teacher, or staff lists.

## Validation

Run from repository root:

```bash
python3 scripts/preflight_upload_check.py
node tests/smoke_check.mjs
```
