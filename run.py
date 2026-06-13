#!/usr/bin/env python3
"""
Index Builder - Python启动脚本
直接用Python运行，避免批处理编码问题
"""
import sys
import os
from pathlib import Path

project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

print("=" * 60)
print("   Index Builder - Quick Start")
print("=" * 60)
print()

print(f"[1/5] Python version: {sys.version.split()[0]}")
if sys.version_info < (3, 9):
    print("[ERROR] Python 3.9+ required")
    input("Press Enter to exit...")
    sys.exit(1)
print("[OK] Python version OK")

print()
print("[2/5] Checking dependencies...")
try:
    import streamlit
    print("[OK] streamlit found")
except ImportError:
    print("[INFO] Installing dependencies...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

print()
print("[3/5] Setting up config...")
config_dir = project_root / "config"
config_dir.mkdir(exist_ok=True)

env_file = config_dir / ".env"
if not env_file.exists():
    env_example = project_root / ".env.example"
    if env_example.exists():
        import shutil
        shutil.copy(env_example, env_file)
        print("[OK] Config file created")

print()
print("[4/5] Checking data...")
data_dir = project_root / "data"
if not data_dir.exists():
    print("[WARN] data directory not found")
else:
    print("[OK] Data directory ready")

print()
print("[5/5] Starting...")
print()
print("=" * 60)
print("   Select an option:")
print("=" * 60)
print()
print("   [1] Dashboard")
print("   [2] Reviewer UI (审核员界面)")
print("   [3] Maintainer UI (维护人员界面)")
print("   [4] Hybrid Retrieval UI (混合检索界面)")
print("   [5] Check Environment")
print("   [0] Exit")
print()
print("=" * 60)
print()

choice = input("Your choice [0-5]: ").strip()

from launcher.launcher import Launcher

launcher = Launcher(project_root=project_root)
launcher.setup_env()

if choice == "1":
    print()
    print("Starting Dashboard...")
    print()
    launcher.launch_dashboard()
elif choice == "2":
    print()
    print("Starting Reviewer UI...")
    print()
    launcher.launch_reviewer()
elif choice == "3":
    print()
    print("Starting Maintainer UI...")
    print()
    launcher.launch_maintainer()
elif choice == "4":
    print()
    print("Starting Hybrid UI...")
    print()
    launcher.launch_hybrid_ui()
elif choice == "5":
    print()
    print("Checking Environment...")
    print()
    launcher.check_python()
    launcher.check_dependencies()
    print()
    input("Press Enter to exit...")
elif choice == "0":
    print("Goodbye!")
else:
    print("Invalid choice")
    input("Press Enter to exit...")
