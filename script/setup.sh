#!/bin/bash
set -e

# 檢查 Python 3.12 (或 python3)
if command -v python3.12 &> /dev/null; then
    PYTHON_CMD="python3.12"
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
else
    echo "錯誤: 找不到 python3.12 或 python3"
    exit 1
fi

echo "使用 Python 指令: $PYTHON_CMD"

# 建立虛擬環境
if [ ! -d ".venv" ]; then
    echo "建立虛擬環境 .venv..."
    $PYTHON_CMD -m venv .venv
else
    echo "虛擬環境 .venv 已存在"
fi

# 升級 pip
echo "升級 pip..."
.venv/bin/pip install --upgrade pip

# 安裝 requirements
echo "安裝套件..."
.venv/bin/pip install -r requirements.txt

echo "====================="
echo "設定完成！"
echo "您可以執行 ./script/run.sh 來啟動伺服器。"
echo "====================="
