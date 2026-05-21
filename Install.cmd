@echo off
title Installing Dependencies for Dpyle
MD WorkFolder
pip install -r requirements.txt
cls
call Start.cmd
