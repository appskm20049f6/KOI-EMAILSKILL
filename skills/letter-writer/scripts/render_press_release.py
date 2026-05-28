#!/usr/bin/env python3
"""把新聞稿變數套進固定模板，輸出 email 主旨、內文與收件清單。

用法：
    python render_press_release.py --vars vars.json [--config config.json]

vars.json 範例：
{
  "date": "2026/05/20",
  "game": "遊戲名稱",
  "version": "S00",
  "update_name": "改版名稱",
  "action": "今日開服",
  "slogan": "主標語○○○",
  "drive_link": "https://drive.google.com/...",
  "recipients": ["media1@example.com", "media2@example.com"]
}

config.json（本機設定，可選）可提供 org_name / title_frame / closing /
signature / recipients 等預設值，vars.json 內的同名欄位會覆蓋它。
"""
import argparse
import json
import sys
from datetime import datetime

WEEKDAYS = ["一", "二", "三", "四", "五", "六", "日"]

DEFAULTS = {
    "org_name": "宇峻奧汀",
    "title_frame": "【宇峻奧汀新聞稿】",
    "closing": "敬請您協助發稿，非常感謝。",
    "signature": "",
    "recipients": [],
}


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def fmt_date(date_str):
    """把 2026/05/20 轉成 2026/05/20(三)。日期格式錯就原樣回傳。"""
    for sep_fmt in ("%Y/%m/%d", "%Y-%m-%d"):
        try:
            d = datetime.strptime(date_str, sep_fmt)
            return f"{date_str}({WEEKDAYS[d.weekday()]})"
        except ValueError:
            continue
    return date_str


def build(vars_data, config):
    cfg = {**DEFAULTS, **config}

    date = fmt_date(vars_data["date"])
    game = vars_data["game"]
    version = vars_data.get("version", "")
    update_name = vars_data.get("update_name", "")
    action = vars_data.get("action", "")
    slogan = vars_data.get("slogan", "")
    drive_link = vars_data.get("drive_link", "")
    title_frame = vars_data.get("title_frame", cfg["title_frame"])
    closing = vars_data.get("closing", cfg["closing"])
    signature = vars_data.get("signature", cfg["signature"])
    recipients = vars_data.get("recipients") or cfg["recipients"]

    # 標題行：日期 + 外框 +《遊戲》版號「改版名」動作！標語！
    name_part = f"《{game}》"
    if version:
        name_part += version
    if update_name:
        name_part += f"「{update_name}」"
    headline = name_part
    if action:
        headline += f"{action}！"
    if slogan:
        headline += f"{slogan}！"

    subject = f"{date} {title_frame}{headline}"

    body_lines = [
        "親愛的媒體朋友您好",
        f" {date} {title_frame}",
        headline,
        "",
        "附件檔案位置",
        drive_link,
        closing,
    ]
    if signature:
        body_lines += ["", signature]
    body = "\n".join(body_lines)

    return subject, body, recipients


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vars", required=True, help="本次發稿變數 JSON")
    ap.add_argument("--config", help="本機設定 JSON（可選）")
    args = ap.parse_args()

    vars_data = load_json(args.vars)
    config = load_json(args.config) if args.config else {}

    try:
        subject, body, recipients = build(vars_data, config)
    except KeyError as e:
        print(f"缺少必要欄位：{e}", file=sys.stderr)
        sys.exit(1)

    print("=== 主旨 (Subject) ===")
    print(subject)
    print()
    print("=== 內文 (Body) ===")
    print(body)
    print()
    print("=== 收件人 (To) ===")
    if recipients:
        for r in recipients:
            print(r)
    else:
        print("(尚未設定媒體聯絡清單)")


if __name__ == "__main__":
    main()
