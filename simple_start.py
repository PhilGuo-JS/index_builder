#!/usr/bin/env python3
"""
Index Builder - 最简单的启动方式
直接调用 streamlit，不经过 launcher
"""
import sys
import os
import time
import webbrowser
import subprocess
from pathlib import Path

project_root = Path(__file__).parent
os.chdir(project_root)

print("=" * 60)
print("   Index Builder - Simple Start")
print("=" * 60)
print()
print("   Select an option:")
print()
print("   [1] Dashboard")
print("   [2] Reviewer UI (审核员界面)")
print("   [3] Maintainer UI (维护人员界面)")
print("   [4] Hybrid Retrieval UI (混合检索界面)")
print("   [0] Exit")
print()
print("=" * 60)
print()

choice = input("Your choice [0-4]: ").strip()

scripts = {
    "1": "launcher/dashboard.py",
    "2": "src/reviewer_workflow.py",
    "3": "src/maintainer_workflow.py",
    "4": "src/hybrid_retrieval_ui.py",
}

if choice == "0":
    print("Goodbye!")
    sys.exit(0)

if choice not in scripts:
    print("Invalid choice")
    sys.exit(1)

script_path = scripts[choice]

print()
print("=" * 60)
print(f"   Starting: {script_path}")
print("=" * 60)
print()
print("[INFO] Waiting 2 seconds...")
time.sleep(2)

# 直接调用 streamlit
cmd = [
    sys.executable, "-m", "streamlit", "run",
    script_path,
    "--server.port", "8501",
    "--server.headless", "false",
    "--server.enableCORS", "false"
]

print(f"[INFO] Running: {' '.join(cmd)}")
print()
print("=" * 60)
print("   The browser should open automatically in 3-5 seconds")
print("   If not, open: http://127.0.0.1:8501")
print("=" * 60)
print()

# 先等一下，然后打开浏览器
def open_browser():
    time.sleep(4)
    url = "http://127.0.0.1:8501"
    print(f"[INFO] Opening browser: {url}")
    try:
        webbrowser.open(url)
    except:
        print(f"[INFO] Please open manually: {url}")

# 在后台打开浏览器
import threading
threading.Thread(target=open_browser, daemon=True).start()

# 启动 streamlit
try:
    subprocess.run(cmd, cwd=str(project_root))
except KeyboardInterrupt:
    print("\n[INFO] Stopped by user")
except Exception as e:
    print(f"\n[ERROR] {e}")
    print("\n[INFO] Trying alternative method...")
    os.system(f"{sys.executable} -m streamlit run {script_path}")
