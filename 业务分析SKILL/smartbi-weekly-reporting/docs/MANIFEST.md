# Manifest - SmartBI Weekly Reporting

## Included

| File | Purpose |
| --- | --- |
| `README.md` | Public-safe project positioning and private-boundary explanation. |
| `references/cli-workflow.md` | CLI workflow layers: doctor, smoke check, route query, export, report build, and writeback guard. |
| `references/security-boundary.md` | SmartBI-specific public safety boundary. |

## Not Included

- SmartBI credentials, report IDs, tenant URLs, internal route maps, BI exports, screenshots, logs, or run artifacts.
- Real cost, revenue, order, customer, student, parent, or teacher data.

## Validation

Run from repository root:

```bash
python3 scripts/preflight_upload_check.py
node tests/smoke_check.mjs
```
