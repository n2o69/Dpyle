
# Dpyle
A tool used to view the code of executables compiled with PyInstaller🐍.

![Python](https://img.shields.io/badge/language-Python-blue?logo=python&logoColor=white)

## Screenshot
<img width="922" height="516" alt="image" src="https://github.com/user-attachments/assets/5027da36-c17e-4ae1-b039-f4a7340e670f" />

## Why Dpyle is better than [Uncompyle](https://github.com/n2o69)

Uncompyle is harder to setup because it need to setup a web server AND an backend server.
Dpyle is a command-line application (CLI), so it doesn't require a web server, and you run the backend on your own computer, which is better for running Pylingual, which requires a lot of resources.

# How to install

 1. Install Python (dev on python 3.13)
 2. Launch `install.cmd`

# Used projects

 - [**pyinstxtractor-ng**](https://github.com/pyinstxtractor/pyinstxtractor-ng)
   A tool that allows you to extract the contents of a PyInstaller archive. In Dpyle, this is pyinstxtractor-ng.exe. It is compiled to make Dpyle more compatible and stable. However, you can still [view its source code](https://github.com/pyinstxtractor/pyinstxtractor-ng).

- [**Pylingual**](https://github.com/syssec-utd/pylingual)
  A tool that allows you to decomile compiled Python files (.pyc)
