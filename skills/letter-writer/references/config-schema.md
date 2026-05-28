# 設定檔 config.json 格式

第一次使用時，向使用者問完設定後，存成下列結構。之後每次發稿先讀此檔帶入預設值。

```json
{
  "org_name": "宇峻奧汀",
  "title_frame": "【宇峻奧汀新聞稿】",
  "sender": {
    "name": "王小明",
    "title": "公關專員",
    "email": "pr@example.com",
    "phone": "02-1234-5678"
  },
  "closing": "敬請您協助發稿，非常感謝。",
  "signature": "",
  "recipients": [
    { "name": "媒體一", "email": "media1@example.com" },
    { "name": "媒體二", "email": "media2@example.com" }
  ],
  "games": [
    "遊戲名稱"
  ]
}
```

## 欄位說明

| 欄位 | 用途 | 預設 |
|------|------|------|
| `org_name` | 發稿單位名稱 | 宇峻奧汀 |
| `title_frame` | 標題外框（夾在日期與內容之間） | 【宇峻奧汀新聞稿】 |
| `sender` | 寄件人姓名、職稱、聯絡方式（用於署名與自我介紹） | 必填 |
| `closing` | 信件固定結尾語 | 敬請您協助發稿，非常感謝。 |
| `signature` | 信末額外署名區塊（可留空） | 空 |
| `recipients` | 媒體聯絡清單，每筆含 `name` 與 `email` | 必填 |
| `games` | 常用遊戲產品清單，方便發稿時挑選 | 可空 |

## 第一次設定問答建議

一次列出讓使用者一起回答即可，不必逐條：

1. 發稿單位名稱？（直接 Enter 用「宇峻奧汀」）
2. 你的姓名與職稱？
3. 你的聯絡 email 與電話？
4. 媒體聯絡清單：請給每個媒體的名稱與 email（可多筆）。
5. 固定結尾語？（直接 Enter 用「敬請您協助發稿，非常感謝。」）
6. 常用的遊戲產品有哪些？（可多筆，可略過）
7. 新聞稿標題外框？（直接 Enter 用「【宇峻奧汀新聞稿】」）

## 給腳本使用時的注意

`render_press_release.py` 的 `--config` 直接吃這個檔。其中 `recipients` 在傳給腳本前，
若要套用，會由 SKILL 流程把 `[{name,email}]` 轉成 email 字串陣列；或在本次變數 JSON 內
直接指定 `recipients` 為 email 陣列以覆蓋。
