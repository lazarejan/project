@echo off
REM ----------------------------------------------------------
REM  E-PASS Windows Setup Script
REM  Installs virtualenv (if missing), sets up venv, and installs requirements
REM ----------------------------------------------------------

REM Change to the directory where the batch file is located
cd /d "%~dp0"

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

REM Check if requirements.txt exists
if not exist "requirements.txt" (
    echo ❌ requirements.txt file not found in current directory!
    echo Current directory: %CD%
    echo Please ensure requirements.txt exists in the project root.
    pause
    exit /b
)

pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to install requirements.
    pause
    exit /b
)

echo.
echo ============================================
echo 🗄️  Initializing database...
echo ============================================
echo Run the database initializer...
echo Creating mydatabase.db ...

REM Use relative paths with the activated virtual environment
python database.py
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to run database.py
    pause
    exit /b
)

echo Generate data for database...
python generator.py
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to run generator.py
    pause
    exit /b
)

echo.
echo ✅ Setup complete!
echo --------------------------------------------
echo To activate the virtual environment later:
echo     venv\Scripts\activate
echo To run the app:
echo     startup.bat
echo --------------------------------------