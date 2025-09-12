@echo off
echo =======================================
echo   Uruchamianie projektu formularza.
echo =======================================
REM 1. Tworzymy wirtualne środowisko
python -m venv venv
echo =======================================
echo    Wirtualne srodowisko utworzone.
echo =======================================
REM 2. Aktywujemy środowisko
call venv\Scripts\activate
echo =======================================
echo    Wirtualne srodowisko aktywowane.
echo ============================================================================================================================================================
REM 3. Instalujemy Flask (jeśli nie ma)
pip install flask
echo ============================================================================================================================================================
echo   Flask zainstalowany i uruchomiony.
echo =======================================
REM 4. Uruchamiamy aplikację
python app.py
echo =======================================
echo         Aplikacja uruchomiona.
echo =======================================
pause