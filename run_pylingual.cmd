@echo off

call "%~dp0pylingual-main\venv\Scripts\activate.bat"

poetry -C "%~dp0pylingual-main" run pylingual ../"%1" -o ../"%2" --trust-lnotab

exit