# 排程：指定時間自動產出新聞稿

採「待發清單 + 真實排程」雙軌：清單一定要寫（穩定、可查），真實排程在環境支援時才建立。

## 待發清單 schedule.json

存在 `~/.claude/letter-writer/schedule.json`。每筆待發稿存進 `pending` 陣列：

```json
{
  "pending": [
    {
      "id": "20260520-game-s00",
      "send_at": "2026-05-20 10:00",
      "status": "scheduled",
      "vars": {
        "date": "2026/05/20",
        "game": "遊戲名稱",
        "version": "S00",
        "update_name": "改版名稱",
        "action": "今日開服",
        "slogan": "主標語○○○",
        "drive_link": "https://drive.google.com/...",
        "recipients": ["media1@example.com", "media2@example.com"]
      }
    }
  ]
}
```

- `id`：建議用「日期-遊戲-版號」組合，方便辨識。
- `send_at`：預定產出/寄送時間。
- `status`：`scheduled`（待發）/ `done`（已產出）/ `cancelled`。
- `vars`：完整本次變數，屆時直接餵給 `render_press_release.py`。

使用者隨時可問「有哪些稿待發」，讀此檔列出 `status == scheduled` 的項目即可。

## 建立真實排程

依環境可用的工具擇一。觸發時要做的事固定：**讀取對應 `id` 的 vars → 跑 render 腳本 → 呈現/寄出 → 把該筆 status 改成 done。**

### 方式一：/schedule（建議，跨對話）
適合「未來某個時間點跑一次」或「每天固定時間檢查」。請使用 `schedule` skill 建立一個排程代理，提示詞範例：

> 在 2026-05-20 10:00 執行：讀取 ~/.claude/letter-writer/schedule.json 中 id 為
> "20260520-game-s00" 的紀錄，用 letter-writer skill 的 render_press_release.py
> 產出新聞稿並呈現給我，完成後把該筆 status 改為 done。

### 方式二：scheduled-tasks MCP
若有 `create_scheduled_task` 工具，建立同樣內容的排程任務，cron/時間設為 `send_at`。

### 環境不支援時
明確告訴使用者：「已登記到待發清單，但目前環境無法自動觸發。到時間請開 Claude，說『產出待發清單裡的 XXX』即可。」不要假裝排程成功。

## 注意
- 真實排程的觸發環境（尤其雲端排程代理）不一定讀得到本機 `~/.claude/...`。若使用雲端排程，需把 vars 一併寫進排程提示詞本身，或改用本機可常駐的排程方式。建立前先確認該環境能存取本機設定檔，存取不到就退回「待發清單 + 手動觸發」。
- 真正寄送 email 需另接 email 工具（如 Gmail MCP）；本 skill 預設只「產出可複製的信件內容」，是否自動寄出由使用者決定。
