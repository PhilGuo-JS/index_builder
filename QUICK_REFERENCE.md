# Index Builder - Quick Reference
# 快速参考

---

## 🚀 How to Start
## 如何启动

### Windows
**Double-click one of these (recommended order):**

| File | Description |
|------|-------------|
| `EASY_START.bat` | ⭐ Easiest - Try this first! |
| `START_SIMPLE.bat` | Simple start |
| `QUICK_START.bat` | Quick start (uses run.py) |

### Or run manually in command line:
```bash
# Dashboard
streamlit run launcher/dashboard.py

# Reviewer UI
streamlit run src/reviewer_workflow.py

# Maintainer UI
streamlit run src/maintainer_workflow.py

# Hybrid UI
streamlit run src/hybrid_retrieval_ui.py
```

---

## 📁 Active Files
## 在用文件

### Launcher Files
- `launcher/launcher.py` - Launcher core
- `launcher/dashboard.py` - Dashboard UI
- `launcher/__init__.py` - Package file

### UI Files
- `src/reviewer_workflow.py` - Reviewer UI ⭐
- `src/maintainer_workflow.py` - Maintainer UI ⭐
- `src/hybrid_retrieval_ui.py` - Hybrid Retrieval UI ⭐

### Launch Scripts
- `EASY_START.bat` - ⭐ Recommended
- `START_SIMPLE.bat` - Simple start
- `QUICK_START.bat` - Quick start
- `run.py` - Python launcher
- `simple_start.py` - Simple Python launcher

### Scripts Folder
- `scripts/run_reviewer.bat` - Reviewer start
- `scripts/run_maintainer.bat` - Maintainer start
- `scripts/run_hybrid_ui.bat` - Hybrid UI start
- `scripts/run_reviewer.sh` - Linux/Mac
- `scripts/run_maintainer.sh` - Linux/Mac
- `scripts/run_hybrid_ui.sh` - Linux/Mac

### Config
- `config/.env` - Config file (auto-created)
- `.env.example` - Config template

---

## 🗂️ Legacy Files (in _legacy folder)
## 遗留文件（在 _legacy 文件夹）

If you need any of these, they're in `_legacy/` folder.

### Legacy Scripts
- Old .bat/.sh files for unused UI

---

## 📝 Documentation
## 文档

- `FILE_CLEANUP_REPORT.md` - File cleanup assessment
- `📖 使用说明.md` - Usage guide (Chinese)
- `README.md` - Original README

---

## ⚠️ Troubleshooting
## 故障排除

### Browser says "Connection Timed Out"
1. Wait 10-15 seconds
2. Refresh the page (F5)
3. Or manually open: http://127.0.0.1:8501

### Can't find Python
- Install Python 3.9+
- Make sure "Add Python to PATH" is checked during installation
- Or try `py` instead of `python`

---

## 🎯 Summary
## 总结

**Just double-click `EASY_START.bat` and you're good to go!**
