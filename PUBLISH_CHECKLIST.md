# Publish Checklist

提交或上传前确认：

- [ ] 新项目已加入 `PROJECTS.md`。
- [ ] 新项目有 README。
- [ ] 关键项目有 `docs/MANIFEST.md` 或 `docs/HANDOFF.md`。
- [ ] 没有 `.env`、Token、Cookie、Webhook、私钥、账号密码。
- [ ] 没有真实合同、客户、学生、家长、供应商、订单、报价、营收、成本或利润数据。
- [ ] 没有原始导出、真实工作簿、截图、录屏、日志、浏览器缓存。
- [ ] 示例数据是 fake sample 或公开安全样例。
- [ ] `python3 scripts/preflight_upload_check.py` 通过。
- [ ] `node tests/smoke_check.mjs` 通过。
- [ ] `git diff --check` 通过。

如果任一项不满足，先修复，不要推送。
