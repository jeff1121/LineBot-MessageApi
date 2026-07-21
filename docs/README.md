# LINE Message API Webhook Console 測試工具

## 專案簡介
本專案是一個輕量級的開發輔助工具，專門用於接收並解析 LINE Message API 的 Webhook 事件。透過將接收到的 JSON Payload 結構化，並以精美的 Rich Console Table 呈現於終端機，開發者可以即時且直觀地檢視 Webhook 事件詳細內容，大幅加速 LINE Bot 應用的開發與除錯過程。

## 技術規格與架構說明
本專案基於現代化 Python 生態系打造，主要技術選型包含：

- **語言**：Python 3.12，利用最新語法特性與強型別提示。
- **Web 框架**：[FastAPI](https://fastapi.tiangolo.com/)，提供高效能且易於開發的非同步 HTTP 伺服器，負責接收 Webhook 請求。
- **資料解析**：內建的 `dataclasses`，用於建立嚴謹的資料模型，將複雜的 LINE Webhook Payload 反序列化為結構化物件。
- **終端機介面**：[Rich](https://rich.readthedocs.io/)，負責在終端機中繪製美觀的表格、高亮語法與排版，提升閱讀體驗。

## 安裝與啟動指引

專案提供了自動化腳本來簡化環境設定與啟動流程。請在專案根目錄下執行以下指令：

### 1. 環境設定與安裝
執行 `setup.sh` 腳本以建立虛擬環境並安裝所需依賴套件：
```bash
bash ./script/setup.sh
```

### 2. 啟動 Webhook Console 伺服器
執行 `run.sh` 腳本啟動 FastAPI 伺服器：
```bash
bash ./script/run.sh
```
預設伺服器將在 `http://localhost:8000` 運行，並準備接收 Webhook 事件。

## 測試指引

為了方便測試，我們提供了一個模擬發送 Webhook 訊息的測試腳本 `test_send.py`。

在伺服器運行期間，開啟另一個終端機視窗，執行：
```bash
python ./script/test_send.py
```
此腳本將會模擬不同類型的 LINE Webhook 事件 (例如文字訊息、圖片訊息、關注事件等)，並發送至本機伺服器。您可以觀察運行中的 Webhook Console 伺服器是否正確解析並印出美觀的表格內容。

## Webhook API 規格說明

本工具提供一個主要的端點來接收 LINE 伺服器的請求。

- **Endpoint**: `POST /callback`
- **Headers**: 需包含 `x-line-signature` 用於驗證 (在測試工具中預設為寬鬆模式或可配置)。
- **Payload 接收格式範例**:

```json
{
  "destination": "Uxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "events": [
    {
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "type": "message",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "message": {
        "id": "325708",
        "type": "text",
        "text": "Hello, world!"
      }
    }
  ]
}
```
伺服器接收到上述格式後，將會自動剖析 `events` 陣列內的事件類型，並渲染輸出至終端機面板上。

- **Endpoint**: `GET /health`
- **功能**: 健康檢查與系統資源即時狀態監控 (CPU、Memory、Disk IOPS)
- **回應範例**:
```json
{
  "status": "healthy",
  "cpu": {
    "used_percent": 18.3,
    "core_count": 14
  },
  "memory": {
    "used_percent": 60.9,
    "total_gb": 36.0,
    "used_gb": 17.71,
    "available_gb": 14.07
  },
  "disk_iops": {
    "read_iops": 59.16,
    "write_iops": 0.0,
    "total_iops": 59.16
  }
}
```
