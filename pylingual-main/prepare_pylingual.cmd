cd /d "%~dp0"

if exist venv del /Q "venv\*"
Python312\python.exe -m pip install virtualenv
Python312\python.exe -m virtualenv venv
call %~dp0venv\Scripts\activate.bat
pip install poetry>=2.0
poetry lock
poetry install
pause