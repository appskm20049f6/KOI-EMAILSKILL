# 固定設定格式（claude.ai 版）

新聞稿用到的固定資訊。在 claude.ai，對話之間不會自動保存，建議把下列內容放進 Project（專案）的自訂指令，或於對話中提供／上傳成 `config.json`。

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
  "games": ["遊戲名稱"]
}
```

| 欄位 | 用途 | 預設 |
|------|------|------|
| `org_name` | 發稿單位名稱 | 宇峻奧汀 |
| `title_frame` | 標題外框 | 【○○新聞稿】 |
| `sender` | 寄件人姓名、職稱、聯絡方式 | 必填 |
| `closing` | 固定結尾語 | 敬請您協助發稿，非常感謝。 |
| `signature` | 信末額外署名（可空） | 空 |
| `recipients` | 媒體聯絡清單，每筆含 `name` 與 `email` | 必填 |
| `games` | 常用遊戲清單 | 可空 |

## 給腳本使用

`render_press_release.py` 的 `--config` 直接吃這個檔。其中 `recipients` 若要傳給腳本，
請把 `[{name,email}]` 轉成 email 字串陣列，或在本次 `vars.json` 內直接放
`recipients` 為 email 陣列以覆蓋。

## 建議：用 Project 一勞永逸

把上面 JSON（或等效的條列）貼進 claude.ai Project 的自訂指令，例如：

> 我是宇峻奧汀公關。發新聞稿時，固定寄件人為○○、媒體清單為 a@x.com、b@y.com、
> 結尾語用「敬請您協助發稿，非常感謝。」、標題外框用「【宇峻奧汀新聞稿】」。

之後在該 Project 內的每次對話，skill 都讀得到，不必重填。
