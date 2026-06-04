# Manifest - Local AI Manager

## Included

| File | Purpose |
| --- | --- |
| `README.md` | Public-safe project positioning and reuse boundary. |
| `references/context-health-check.md` | Codex context, skill directory, automation config, and security hygiene check method. |

## Not Included

- Raw Codex sessions, local scan reports, auth files, environment values, logs, shell history, or automation private configs.

## Validation

Run from repository root:

```bash
python3 scripts/preflight_upload_check.py
node tests/smoke_check.mjs
```
