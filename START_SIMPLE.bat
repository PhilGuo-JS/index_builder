@echo off
echo ========================================
echo   Index Builder - Simple Start
echo ========================================
echo.

cd /d "%~dp0"

echo Trying to start...
echo.

python simple_start.py
if errorlevel 1 (
    echo.
    echo 'python simple_start.py' failed, trying 'py simple_start.py'...
    echo.
    py simple_start.py
    if errorlevel 1 (
        echo.
        echo ========================================
        echo   FAILED TO START
        echo ========================================
        echo.
        echo Let's try directly with streamlit...
        echo.
        echo Available options:
        echo   1. Dashboard: streamlit run launcher/dashboard.py
        echo   2. Reviewer: streamlit run src/reviewer_workflow.py
        echo   3. Maintainer: streamlit run src/maintainer_workflow.py
        echo   4. Hybrid UI: streamlit run src/hybrid_retrieval_ui.py
        echo.
        pause
    )
)
