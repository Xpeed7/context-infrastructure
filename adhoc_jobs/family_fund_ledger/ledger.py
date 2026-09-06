#!/usr/bin/env python3
"""Record family fund expenses and render a plain-text summary."""

from __future__ import annotations

import argparse
import json
import re
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


DATE_PATTERN = re.compile(r"^(?P<year>\d{4})-(?P<month>0[1-9]|1[0-2])(?:-(?P<day>0[1-9]|[12]\d|3[01]))?$")


def load_ledger(path: Path) -> dict:
    with path.open(encoding="utf-8") as file:
        ledger = json.load(file)
    if not isinstance(ledger.get("opening_balance"), int) or ledger["opening_balance"] < 0:
        raise ValueError("opening_balance 必须是非负整数")
    if not isinstance(ledger.get("entries"), list):
        raise ValueError("entries 必须是数组")
    return ledger


def save_ledger(path: Path, ledger: dict) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(ledger, file, ensure_ascii=False, indent=2)
        file.write("\n")


def validate_date(value: str) -> tuple[str, str]:
    match = DATE_PATTERN.fullmatch(value)
    if not match:
        raise ValueError("日期必须是 YYYY-MM 或 YYYY-MM-DD")

    year = int(match.group("year"))
    month = int(match.group("month"))
    day_text = match.group("day")
    if day_text:
        day = int(day_text)
        if day > 29 and month == 2:
            raise ValueError("日期不是有效的自然日")
        if day == 31 and month in {4, 6, 9, 11}:
            raise ValueError("日期不是有效的自然日")
        if month == 2 and day == 29 and year % 4 != 0:
            raise ValueError("日期不是有效的自然日")
        return value, "day"
    return value, "month"


def summarize(ledger: dict) -> dict:
    total_spent = sum(entry["amount"] for entry in ledger["entries"])
    opening_balance = ledger["opening_balance"]
    remaining = opening_balance - total_spent
    usage = (Decimal(total_spent) / Decimal(opening_balance) * Decimal("100")).quantize(
        Decimal("0.1"), rounding=ROUND_HALF_UP
    ) if opening_balance else Decimal("0.0")
    return {
        "opening_balance": opening_balance,
        "total_spent": total_spent,
        "remaining": remaining,
        "usage_percent": usage,
    }


def format_message(ledger: dict, as_of: str) -> str:
    summary = summarize(ledger)
    lines = [
        "💰【小金库使用情况】",
        f"截至：{as_of}",
        "",
        f"🏦 初始金额：{summary['opening_balance']}元",
        f"📤 累计支出：{summary['total_spent']}元",
        f"🪙 剩余金额：{summary['remaining']}元",
        f"📊 已使用：{summary['usage_percent']}%",
        "",
        "🧾 账单明细：",
    ]
    for entry in sorted(ledger["entries"], key=lambda item: (item["date"], item["id"])):
        icon = "🛡️" if "险" in entry["item"] else "📚"
        lines.append(f"{icon} {entry['date']} {entry['person']}｜{entry['item']}｜{entry['amount']}元")
    lines.extend(["", "由AI（ChatGPT）计算并发送"])
    return "\n".join(lines)


def add_entry(ledger: dict, date: str, person: str, item: str, amount: int) -> dict:
    date, precision = validate_date(date)
    if not person.strip() or not item.strip():
        raise ValueError("person 和 item 不能为空")
    if amount <= 0:
        raise ValueError("amount 必须大于 0")

    duplicate = any(
        entry["date"] == date
        and entry["person"] == person
        and entry["item"] == item
        and entry["amount"] == amount
        for entry in ledger["entries"]
    )
    if duplicate:
        raise ValueError("检测到完全相同的账单，已拒绝重复记账")

    entry = {
        "id": f"entry-{len(ledger['entries']) + 1:03d}",
        "date": date,
        "date_precision": precision,
        "person": person,
        "item": item,
        "amount": amount,
    }
    ledger["entries"].append(entry)
    return entry


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="小金库记账工具")
    parser.add_argument(
        "--data",
        type=Path,
        default=Path(__file__).with_name("ledger.json"),
        help="账本 JSON 文件路径",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    summary_parser = subparsers.add_parser("summary", help="输出汇总 JSON")
    summary_parser.set_defaults(command_handler="summary")

    message_parser = subparsers.add_parser("message", help="输出给家人的纯文本同步消息")
    message_parser.add_argument("--as-of", required=True, help="消息截至日期，格式 YYYY-MM-DD")
    message_parser.set_defaults(command_handler="message")

    add_parser = subparsers.add_parser("add", help="新增一笔账单")
    add_parser.add_argument("--date", required=True, help="账单日期，格式 YYYY-MM 或 YYYY-MM-DD")
    add_parser.add_argument("--person", required=True, help="孩子姓名")
    add_parser.add_argument("--item", required=True, help="支出项目")
    add_parser.add_argument("--amount", required=True, type=int, help="金额，单位为元")
    add_parser.set_defaults(command_handler="add")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    ledger = load_ledger(args.data)

    if args.command_handler == "summary":
        summary = summarize(ledger)
        summary["usage_percent"] = str(summary["usage_percent"])
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return

    if args.command_handler == "message":
        validate_date(args.as_of)
        print(format_message(ledger, args.as_of))
        return

    entry = add_entry(ledger, args.date, args.person, args.item, args.amount)
    save_ledger(args.data, ledger)
    print(json.dumps(entry, ensure_ascii=False, indent=2))
    print(format_message(ledger, args.date))


if __name__ == "__main__":
    main()
