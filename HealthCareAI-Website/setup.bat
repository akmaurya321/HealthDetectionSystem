@echo off
echo Setting up DeepCareX...
echo.

if exist "database\DeepCareX.db" (
    echo Removing old database...
    del "database\DeepCareX.db"
)

echo Creating database...
python database.py

echo.
echo Starting application...
python main.py

pause