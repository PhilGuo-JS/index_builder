# File Cleanup Assessment Report
# 文件清理评估报告

> **WARNING**: 请谨慎删除！建议先备份或重命名，确认没问题后再删除。

---

## 📊 Current Active Files (DO NOT DELETE)
## 当前在用文件（**不要删除**）

### UI 界面
- `src/reviewer_workflow.py` - 审核员界面（在用）
- `src/maintainer_workflow.py` - 维护人员界面（在用）
- `src/hybrid_retrieval_ui.py` - 混合检索界面（在用）

### Launcher Files (New)
- `launcher/launcher.py` - 启动器核心（新增）
- `launcher/dashboard.py` - 管理面板（新增）
- `launcher/__init__.py` - 包文件（新增）
- `run.py` - Python 启动脚本（新增）
- `QUICK_START.bat` - 快速启动（新增）
- `START.bat` - 备用启动器（新增）

### Scripts
- `scripts/run_reviewer.bat/sh` - 审核员启动脚本（在用）
- `scripts/run_maintainer.bat/sh` - 维护人员启动脚本（在用）
- `scripts/run_hybrid_ui.bat/sh` - 混合检索启动脚本（在用）

### Core Source
- `requirements.txt` - 依赖列表
- `.env.example` - 配置示例
- `src/__init__.py` - 包文件

---

## ⚠️ Legacy Files (Review Before Deletion)
## 遗留文件（请评估后再删除）

### Legacy UI Files (Likely Obsolete)
### 旧版 UI 文件（很可能已过时）
```
src/review_app.py              - 旧审核界面
src/intent_catalog_editor.py   - 旧编辑器
src/intent_catalog_workbench.py- 旧工作台
src/main_assign.py            - 旧分配脚本
```

### Legacy Scripts (Likely Obsolete)
### 旧版脚本（很可能已过时）
```
scripts/run_editor.bat/sh
scripts/run_workbench.bat/sh
scripts/run_review_app.bat/sh
scripts/run_review_cli.bat/sh
scripts/run_enrich_catalog*.bat/sh
scripts/run_collect_feedback*.bat/sh
scripts/run_prepare_catalog_pipeline.bat/sh
scripts/run_build_intent_fields.bat/sh
scripts/run_assign_query_to_intent.bat/sh
scripts/run_split_catalog.bat/sh
```

### Legacy Source in src/main/
### src/main/ 下的旧脚本（需要评估）
```
src/main/run_review_cli.py
src/main/run_prepare_catalog_pipeline.py
src/main/run_split_intent_catalog.py
src/main/run_collect_catalog_feedback.py
src/main/run_enrich_intent_catalog.py
src/main/run_build_intent_fields.py
src/main/run_assign_query_to_intent.py
```

### Other Legacy Files
### 其他遗留文件
```
调试启动.bat
简单测试.bat
启动.bat
启动.sh
TEST_PYTHON.bat
```

---

## 📝 Documentation Files (Need Review)
## 文档文件（需要评估）

### Possibly Outdated
### 可能已过时
```
README.md                     - 可能需要更新
docs/STREAMLIT_PERFORMANCE_OPTIMIZATION.md
docs/意图目录工作台使用说明.md
documents/*.md               - 需要检查内容
```

---

## 🛠️ Recommended Action Steps
## 建议操作步骤

### Step 1: Backup First
### 第一步：先备份
```bash
# 建议先把整个项目备份一下
# 或者创建一个 legacy 文件夹
mkdir _legacy
```

### Step 2: Move Instead of Delete
### 第二步：移动而非删除
```batch
# Windows
mkdir _legacy_src
move src\review_app.py _legacy_src\
move src\intent_catalog_editor.py _legacy_src\
move src\intent_catalog_workbench.py _legacy_src\

mkdir _legacy_scripts
move scripts\run_editor.bat _legacy_scripts\
move scripts\run_workbench.bat _legacy_scripts\
move scripts\run_review_app.bat _legacy_scripts\
```

### Step 3: Test Everything Works
### 第三步：测试一切正常
- 运行 `QUICK_START.bat`
- 测试三个 UI 都能打开
- 测试关键功能

### Step 4: Delete After Confirmation
### 第四步：确认后再删除
```batch
# 确认没问题后再删除 _legacy_* 文件夹
rmdir /s _legacy_src
rmdir /s _legacy_scripts
```

---

## ❓ Need Your Confirmation
## 需要你确认的问题

1. **Pipeline 脚本**：`src/main/` 下的那些 pipeline 脚本还在用吗？
2. **数据文件**：`data/` 目录下的文件还需要吗？
3. **文档**：哪些文档还需要保留？

---

## 📋 Quick Reference Table
## 快速参考表

| File Group | Status | Action |
|------------|--------|--------|
| reviewer_workflow.py | ✅ Active | Keep |
| maintainer_workflow.py | ✅ Active | Keep |
| hybrid_retrieval_ui.py | ✅ Active | Keep |
| review_app.py | ⚠️ Legacy | Review |
| intent_catalog_editor.py | ⚠️ Legacy | Review |
| intent_catalog_workbench.py | ⚠️ Legacy | Review |
| launcher/* | ✅ New | Keep |
| run.py | ✅ New | Keep |
| QUICK_START.bat | ✅ New | Keep |

---

> 💡 **Tip**: 如果不确定，就先移动到 `_legacy/` 文件夹，用一段时间没问题再删除！
