@echo off
REM ----------------------------------------------------------
REM  E-PASS Application Startup Script
REM  Activates virtual environment and runs the application
REM ----------------------------------------------------------

REM Change to the directory where the batch file is located
cd /d "%~dp0"

echo ============================================
echo 🚀 Starting E-PASS Application...
echo ============================================

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ❌ Virtual environment not found!
    echo Please run setup.bat first to create the virtual environment.
    pause
    exit /b
)

REM Activate virtual environment
echo ⚙️  Activating virtual environment...
call venv\Scripts\activate

REM Check if main.py exists
if not exist "main.py" (
    echo ❌ main.py file not found in current directory!
    echo Current directory: %CD%
    echo Please ensure main.py exists in the project root.
    pause
    exit /b
)

REM Run the application
echo 📱 Running main.py...
python main.py

REM Check if the application ran successfully
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Application failed to run.
    echo Error code: %ERRORLEVEL%
    pause
    exit /b
)

echo ✅ Application finished.
pause