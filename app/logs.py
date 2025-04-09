# app/logs.py
import datetime
import os

LOGGING_ENABLED = True  # Set to False if you want to disable logs in production
LOG_FILE = "chat_logs.txt"

def log_interaction(user_msg, bot_reply, file_path=LOG_FILE):
    if not LOGGING_ENABLED:
        return

    try:
        with open(file_path, "a", encoding="utf-8") as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}]\nUser: {user_msg}\nSafeSathi (GPT): {bot_reply}\n\n")
    except Exception as e:
        print(f"[LOGGING ERROR] Failed to write log: {e}")
