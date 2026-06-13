@echo off
echo ========================================
echo   Index Builder - Quick Start
echo ========================================
echo.

cd /d "%~dp0"

echo Trying to start with Python...
echo.

python run.py
if errorlevel 1 (
    echo.
    echo 'python run.py' failed, trying 'py run.py'...
    echo.
    py run.py
    if errorlevel 1 (
        echo.
        echo ========================================
        echo   FAILED TO START
        echo ========================================
        echo.
        echo Please check:
        echo   1. Python is installed (3.9+)
        echo   2. You're in the right directory
        echo.
        echo Current directory: %CD%
        echo.
        dir /b
        echo.
        pause
    )
)
