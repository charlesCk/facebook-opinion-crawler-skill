# Manifest - Seeyon Contract Draft

## Included

| File | Purpose |
| --- | --- |
| `SKILL.md` | Runtime workflow instruction for creating Seeyon OA contract drafts. |
| `references/config.example.json` | Fake config shape for runtime-only OA credentials and form values. |
| `references/field-checklist.md` | Verification checklist for applicant, parties, amount, finance, and attachment fields. |
| `scripts/create_seeyon_contract_draft.mjs` | Draft-first Playwright automation entrypoint. |
| `agents/openai.yaml` | Public-safe agent config template. |

## Not Included

- Real OA URL, account, password, cookies, session files, or tenant identifiers.
- Real contracts, supplier/customer data, screenshots, traces, logs, or generated drafts.
- Final submit/approval automation. The current workflow saves draft only.

## Validation

Run from repository root:

```bash
node tests/smoke_check.mjs
python3 scripts/preflight_upload_check.py
```
