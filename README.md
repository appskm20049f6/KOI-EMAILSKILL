# letter-writer — 中文新聞稿 / 商務信件產生器 (Claude Code Plugin)

一個 Claude Code Plugin，內含 `letter-writer` skill。主要用途是**依固定模板生成遊戲公司新聞稿發送 email**（如宇峻奧汀發稿給媒體），也能寫一般中文商務信件。輸出純文字，方便直接複製或寄出。

## 特色

- **三層模組化**：固定設定（設一次重複用）＋ 每次發稿變數（每次問）＋ 排程
- **第一次設定**：首次使用會問你發稿單位、寄件人、媒體聯絡清單、結尾語等，存到本機 `~/.claude/letter-writer/config.json`，之後自動帶入
- **每次發稿問答**：每次只需給日期、遊戲、版號、改版名、動作、主標語、Drive 連結，自動套出主旨＋內文＋收件清單（日期週幾自動計算）
- **排程定時產出**：可指定寄送時間，登記待發清單，並在支援的環境建立真實排程，時間到自動生成
- **一般商務信**：另附詢價、合作、跟進、道歉、感謝、通知等模板

## 新聞稿輸出範例

```
主旨：
YYYY/MM/DD(週幾) 【○○新聞稿】《遊戲名稱》S00「改版名稱」今日開服！主標語○○○！

內文：
親愛的媒體朋友您好
 YYYY/MM/DD(週幾) 【○○新聞稿】
《遊戲名稱》S00「改版名稱」今日開服！主標語○○○！

附件檔案位置
https://drive.google.com/drive/folders/...
敬請您協助發稿，非常感謝。
```

## 安裝

### A. Claude Code（給 repo 網址即可）

在 Claude Code 中執行：

```
/plugin marketplace add appskm20049f6/KOI-EMAILSKILL
/plugin install letter-writer@letter-writer-marketplace
```

安裝後重新載入 Claude Code 即可使用。

### B. Cowork（下載單檔安裝）

到本 repo 的 [Releases](https://github.com/appskm20049f6/KOI-EMAILSKILL/releases) 下載：

- `letter-writer.plugin` —— 在 Cowork 對話中拖入此檔，按下安裝按鈕即可
- `letter-writer.skill` —— 若只需單一 skill，亦可下載此檔匯入

兩種檔案內容相同，差別只在 `.plugin` 帶完整外掛清單、`.skill` 只含技能本體。

## 使用方式

直接用自然語言說你要發稿，例如：

- 「幫我發一篇新聞稿，○○遊戲 S00 改版今日開服，5/20 發，連結等等給你。」
- 「排程 5/20 早上 10 點發這篇稿給媒體。」
- 「有哪些稿待發？」

第一次使用會先請你完成設定。設定資料**只存在你本機**，不會上傳到 GitHub，避免媒體 email 外流。

## 結構

```
letter-writer-plugin/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── skills/letter-writer/
│   ├── SKILL.md                      主流程（設定 → 發稿問答 → 生成 → 排程）
│   ├── scripts/
│   │   └── render_press_release.py   套模板、算週幾的渲染腳本
│   └── references/
│       ├── config-schema.md          設定檔格式與第一次問答
│       ├── press-release-template.md  新聞稿模板邏輯與範例
│       ├── scheduling.md             排程與待發清單
│       └── templates.md              一般商務信模板
├── README.md
└── LICENSE
```

## 自訂

- 改新聞稿格式/結尾語：改 `config.json` 或編輯 `scripts/render_press_release.py`
- 改一般商務信模板：編輯 `references/templates.md`

## 授權

MIT License — 歡迎自由使用與分享。
