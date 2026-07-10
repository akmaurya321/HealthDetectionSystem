@echo off
echo Setting up HealthCare AI...
echo.

if exist "database\HealthCareAI.db" (
    echo Removing old database...
    del "database\HealthCareAI.db"
)

echo Creating database...
python database.py

echo.
echo Starting application...
python main.py

pause