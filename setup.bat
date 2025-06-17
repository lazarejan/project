---

## 🧰 `setup.bat` (final version for Windows with `virtualenv`)

```bat
@echo off
REM ----------------------------------------------------------
REM  E-PASS Windows Setup Script
REM  Creates virtual environment and installs requirements
REM ----------------------------------------------------------

echo Creating virtual environment using virtualenv...
virtualenv venv

IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Failed to create virtual environment. Is virtualenv installed?
    echo 💡 Try: pip install virtualenv
    pause
    exit /b
)

echo ✅ Virtual environment created.

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies from requirements.txt...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ✅ Setup complete!
echo --------------------------------------------
echo To activate the virtual environment later:
echo     venv\Scripts\activate
echo To run the app:
echo     python main_ui.py
echo --------------------------------------------
pause
