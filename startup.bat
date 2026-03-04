@echo off
REM Set your email credentials here
set SENDER_EMAIL=your_email@qq.com
set SENDER_PASSWORD=your_qq_smtp_authorization_code

REM Run the Python script with uv
cd /d "%~dp0"
uv run ip_notifier.py

REM Optional: uncomment to see output (remove for silent execution)
REM pause
