# Agent 團隊分工與專案規範

本專案 (LINE Message API Webhook Console) 採用多 Agent 協作模式進行開發，以確保高品質的程式碼與完整的文件。

## Agent 團隊分工架構

專案開發由以下三種主要 Agent 負責：

1. **Documentation Agent (文件 Agent)**
   - **職責**：負責專案所有文件的撰寫、維護與更新。
   - **範圍**：撰寫 `README.md`、架構設計文件、API 規格說明、Agent 規範 (本檔案) 等，並確保文件與最新程式碼同步。

2. **Core Application Agent (核心應用 Agent)**
   - **職責**：負責核心應用程式系統架構與業務邏輯的開發。
   - **範圍**：實作 FastAPI 伺服器、Webhook 接收邏輯、資料解析 (使用 Dataclass)、Rich Console 介面輸出等核心功能。

3. **Script & Automation Agent (腳本與自動化 Agent)**
   - **職責**：負責開發環境建置、自動化腳本與測試工具。
   - **範圍**：撰寫安裝腳本 (`setup.sh`)、啟動腳本 (`run.sh`)、測試模擬工具 (`test_send.py`)，確保開發與測試流程順暢。

## 專案目錄結構規範

為了保持專案結構清晰，所有檔案與目錄應遵循以下規範：

- `./docs/`：文件根目錄。存放所有專案相關文件，例如系統架構說明、API 規格與操作手冊。
- `./src/`：程式碼根目錄。存放核心應用程式的原始碼 (Python)。
- `./script/`：腳本根目錄。存放所有用於安裝、環境設定、專案啟動與模擬測試的自動化腳本。

## 開發規範與 Python 3.12 最佳實踐

本專案採用 Python 3.12 進行開發，請所有 Agent 嚴格遵守以下最佳實踐：

1. **強型別提示 (Type Hinting)**：所有函式與方法均需提供完整的參數與回傳值型別提示，提升程式碼可讀性與靜態檢查能力。
2. **Dataclass 應用**：優先使用 Python 的 `dataclasses` 模組來定義資料結構 (如 Webhook Payload 的解析模型)，減少冗餘程式碼。
3. **最新語法特性**：善用 Python 3.12 的新特性 (例如改進的泛型語法、模式匹配 `match-case`) 以撰寫簡潔且高效的程式碼。
4. **模組化設計**：程式碼應具備高內聚、低耦合特性，依功能拆分至不同模組中。

## 協作模式與擴充原則

1. **模組解耦**：Core Application、腳本與文件應各自獨立。任何 API 或資料結構的修改，需由 Core Application Agent 發起，並由 Documentation Agent 同步更新文件，Script Agent 更新對應的測試腳本。
2. **漸進式擴充**：若需新增功能，請優先建立對應的 Issue 或功能規格，由 Documentation Agent 記錄後，再交由其他 Agent 進行實作。
3. **持續溝通**：Agent 之間需透過明確的介面 (如設定檔、命令列參數或標準輸入輸出) 進行互動，降低系統整體的複雜度。
