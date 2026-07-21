#!/bin/bash

# 檢查 .venv 是否存在
if [ ! -d ".venv" ]; then
    echo "錯誤: 找不到 .venv 目錄，請先執行 ./script/setup.sh"
    exit 1
fi

echo "啟動伺服器..."
export PYTHONPATH=src:$PYTHONPATH
.venv/bin/uvicorn src.main:app --host 0.0.0.0 --port 3000 --reload
