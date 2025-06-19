@echo off
REM ----------------------------------------------------------
REM  E-PASS Windows Setup Script
REM  Installs virtualenv (if missing), sets up venv, and installs requirements
REM ----------------------------------------------------------

echo ============================================
echo 🔧 Checking if virtualenv is installed...
echo ============================================

pip show virtualenv >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❗ virtualenv not found. Installing it now...
    pip install virtualenv

    IF %ERRORLEVEL% NEQ 0 (
        echo ❌ Failed to install virtualenv.
        echo Please ensure pip is available and try again.
        pause
        exit /b
    )
) ELSE (
    echo ✅ virtualenv is already installed.
)

echo.
echo ============================================
echo 🏗️  Creating virtual environment in /venv...
echo ============================================

virtualenv venv
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to create virtual environment.
    pause
    exit /b
)

echo ✅ Virtual environment created.

echo.
echo ============================================
echo ⚙️  Activating virtual environment...
echo ============================================
call venv\Scripts\activate

echo.
echo ============================================
echo 📦 Installing Python dependencies...
echo ============================================
pip install --upgrade pip
pip install -r requirements.txt

IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to install requirements.
    pause
    exit /b
)

echo Run the database  initializer...
echo Creating mydatabase.db ...
c:/Users/User/Desktop/lazare/project/project/venv/Scripts/python.exe database.py
echo Generate data for database...
c:/Users/User/Desktop/lazare/project/project/venv/Scripts/python.exe generator.py

IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to run python files.
    pause
    exit /b
)

echo.
echo ✅ Setup complete!
echo --------------------------------------------
echo To activate the virtual environment later (by default it is activated):
echo     venv\Scripts\activate
echo To run the app:
echo     startup.bat
echo --------------------------------------------
pause
