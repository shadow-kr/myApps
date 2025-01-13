@echo off
REM  ./To_do_web_app_with_flask/runner.bat
set FLASK_APP=.\To_do_web_app_with_flask\to_do_flask.py
set FLASK_ENV=development

echo FLASK_APP=%FLASK_APP%
echo FLASK_ENV=%FLASK_ENV%


flask run

pause
