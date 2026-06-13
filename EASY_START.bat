@echo off
echo ========================================
echo   Index Builder - EASY START
echo ========================================
echo.
cd /d "%~dp0"

echo Here are the commands you can use:
echo.
echo ========================================
echo   Option 1: Dashboard
echo   Run this:
echo     streamlit run launcher/dashboard.py
echo.
echo ========================================
echo   Option 2: Reviewer UI
echo   Run this:
echo     streamlit run src/reviewer_workflow.py
echo.
echo ========================================
echo   Option 3: Maintainer UI
echo   Run this:
echo     streamlit run src/maintainer_workflow.py
echo.
echo ========================================
echo   Option 4: Hybrid UI
echo   Run this:
echo     streamlit run src/hybrid_retrieval_ui.py
echo.
echo ========================================
echo.
echo Let's try to start Option 1 for you automatically...
echo.

timeout /t 2

streamlit run launcher/dashboard.py
if errorlevel 1 (
    echo.
    echo That didn't work. Let's try with 'python -m streamlit'...
    echo.
    python -m streamlit run launcher/dashboard.py
    if errorlevel 1 (
        echo.
        echo Still not working. Let's try 'py -m streamlit'...
        echo.
        py -m streamlit run launcher/dashboard.py
        if errorlevel 1 (
            echo.
            echo ========================================
            echo   Please run one of the commands above
            echo   manually in the command line.
            echo ========================================
            echo.
            pause
        )
    )
)
