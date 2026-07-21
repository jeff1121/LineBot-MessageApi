import sys
from pathlib import Path

# 確保 src 目錄在 sys.path 中
src_dir = Path(__file__).resolve().parent
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

import asyncio
import json
import time
import psutil
import uvicorn
from fastapi import FastAPI, Request, HTTPException, Header, Response
from parser import parse_webhook_payload
from formatter import print_webhook_events
from security import verify_signature
import config

app = FastAPI(title="LINE Webhook 測試工具")

@app.post("/webhook")
@app.post("/callback")
async def webhook_endpoint(request: Request, x_line_signature: str = Header(None)):
    """
    接收來自 LINE Message API 的 Webhook POST 請求 (支援 /webhook 與 /callback)，
    將 Payload 剖析為 Dataclasses 物件並於控制台以 Rich 表格列印。
    """
    body_bytes = await request.body()
    
    # 若啟動簽章驗證則比對 X-Line-Signature
    if config.ENABLE_SIGNATURE_CHECK and not verify_signature(body_bytes, x_line_signature or ""):
        raise HTTPException(status_code=400, detail="Invalid X-Line-Signature")

    try:
        body = json.loads(body_bytes.decode("utf-8")) if body_bytes else {}
    except Exception:
        body = {}
        
    # 解析 Webhook Payload
    payload = parse_webhook_payload(body)
    
    # 於控制台以 Rich 表格印出
    print_webhook_events(payload)
    
    # 回傳 LINE API 所需的 OK 狀態
    return {"status": "ok"}

@app.get("/health")
async def health_check():
    """
    健康檢查端點：回傳伺服器運作狀態以及 CPU、記憶體與 Disk IOPS 之即時數據。
    """
    # 1. CPU 指標
    cpu_percent = psutil.cpu_percent(interval=0.1)
    cpu_percent_str = f"{cpu_percent:.2f}%"
    
    # 2. 記憶體指標
    mem = psutil.virtual_memory()
    memory_status = {
        "used_percent": mem.percent,
        "total_gb": round(mem.total / (1024 ** 3), 2),
        "used_gb": round(mem.used / (1024 ** 3), 2),
        "available_gb": round(mem.available / (1024 ** 3), 2)
    }
    
    # 3. Disk IOPS 指標 (採樣 0.1 秒)
    t1 = time.time()
    io1 = psutil.disk_io_counters()
    await asyncio.sleep(0.1)
    t2 = time.time()
    io2 = psutil.disk_io_counters()
    
    dt = t2 - t1
    if io1 and io2 and dt > 0:
        read_iops = round((io2.read_count - io1.read_count) / dt, 2)
        write_iops = round((io2.write_count - io1.write_count) / dt, 2)
        total_iops = round(read_iops + write_iops, 2)
    else:
        read_iops = write_iops = total_iops = 0.0

    disk_iops_status = {
        "read_iops": read_iops,
        "write_iops": write_iops,
        "total_iops": total_iops
    }

    return {
        "status": "healthy",
        "line_config": {
            "channel_id_configured": bool(config.LINE_CHANNEL_ID),
            "channel_secret_configured": bool(config.LINE_CHANNEL_SECRET),
            "access_token_configured": bool(config.LINE_CHANNEL_ACCESS_TOKEN),
            "signature_check_enabled": config.ENABLE_SIGNATURE_CHECK
        },
        "cpu": {
            "used_percent": cpu_percent_str,
            "core_count": psutil.cpu_count(logical=True)
        },
        "memory": memory_status,
        "disk_iops": disk_iops_status
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
