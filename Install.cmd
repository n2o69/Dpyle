@echo off
title Installing Dependencies for Dpyle
mkdir WorkFolder
pip install -r requirements.txt
powershell -Command ^
"Start-Process -FilePath 'pylingual-main/prepare_pylingual.cmd' -WorkingDirectory pylingual-main -Verb RunAs"
cls

Start Start.cmd
