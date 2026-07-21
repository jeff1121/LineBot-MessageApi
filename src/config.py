import os
from pathlib import Path
from dotenv import load_dotenv

# 自動尋找專案根目錄的 .env 檔案並載入
base_dir = Path(__file__).resolve().parent.parent
env_file = base_dir / ".env"
if env_file.exists():
    load_dotenv(dotenv_path=env_file)
else:
    load_dotenv()

LINE_CHANNEL_ID = os.getenv("LINE_CHANNEL_ID", "")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET", "")
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "")

# 簽章驗證開關 (預設為 false，利於本機測試與模擬工具發送)
ENABLE_SIGNATURE_CHECK = os.getenv("ENABLE_SIGNATURE_CHECK", "false").lower() in ("true", "1", "yes")

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
