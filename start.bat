@echo off
title 智能字幕提取器

echo 正在启动智能字幕提取器...
echo.
echo 请确保已安装以下依赖：
echo - Python 3.8+
echo - FFmpeg
echo - OLLAMA（可选，用于字幕优化）
echo.
echo 正在检查Python环境...

python --version
if errorlevel 1 (
    echo 错误：未找到Python，请确保Python已安装并添加到PATH
    pause
    exit /b 1
)

echo.
echo 正在安装依赖...
pip install -r requirements.txt

echo.
echo 启动应用...
python app.py

echo.
echo 应用已关闭，按任意键退出...
pause