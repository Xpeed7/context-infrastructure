# Family Fund Ledger

记录牛牛和桐桐的学习、保险等小金库收支。账本数据保存在 `ledger.json`，脚本只使用 Python 标准库。

## 用法

查看汇总：

```bash
python3 ledger.py summary
```

新增账单：

```bash
python3 ledger.py add --date 2026-09-06 --person 牛牛 --item 成都学舞 --amount 1000
```

新增收入：

```bash
python3 ledger.py add --date 2026-09-13 --person 小金库 --item 新增收入 --amount 6000 --type income
```

日期支持 `YYYY-MM` 和 `YYYY-MM-DD`。脚本会拒绝完全相同的重复账单。

生成发送给家人的同步消息：

```bash
python3 ledger.py message --as-of 2026-09-05
```

微信发送由当前对话在本机已登录的微信桌面端完成，账本脚本不保存微信凭据。
