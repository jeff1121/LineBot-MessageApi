import base64
import hashlib
import hmac
from config import LINE_CHANNEL_SECRET, ENABLE_SIGNATURE_CHECK

def verify_signature(body_bytes: bytes, signature: str) -> bool:
    """
    驗證 LINE Webhook 的 X-Line-Signature HMAC-SHA256 簽章。
    若未開啟簽章檢查 (ENABLE_SIGNATURE_CHECK=False) 或未設定 CHANNEL_SECRET，預設回傳 True 以利本機測試。
    """
    if not ENABLE_SIGNATURE_CHECK or not LINE_CHANNEL_SECRET:
        return True

    if not signature:
        return False

    hash_val = hmac.new(
        LINE_CHANNEL_SECRET.encode("utf-8"),
        body_bytes,
        hashlib.sha256
    ).digest()
    
    expected_signature = base64.b64encode(hash_val).decode("utf-8")
    return hmac.compare_digest(expected_signature, signature)
