##################################################################
# Imports
##################################################################
import subprocess
import os
import shutil
import sys
import random
from pathlib import Path
from pystyle import Colors, Colorate, Center, System, Write
from colorama import Fore, init
from shutil import get_terminal_size
import json
import webview
import time
##################################################################
#  Utilities
##################################################################

class Display:
    def ShowTitleScreen():
        print(Center.XCenter(Colorate.Vertical(Colors.blue_to_purple, """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░       ░░░       ░░░  ░░░░  ░░  ░░░░░░░░        ░
▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒▒  ▒▒  ▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒
▓  ▓▓▓▓  ▓▓       ▓▓▓▓▓    ▓▓▓▓  ▓▓▓▓▓▓▓▓      ▓▓▓
█  ████  ██  ███████████  █████  ████████  ███████
█       ███  ███████████  █████        ██        █
██████████████████████████████████████████████████
                                               """, 1)))
        width = get_terminal_size().columns
        line = "─" * width
        print(Colorate.Horizontal(Colors.rainbow, line))

    Question = f"{Fore.BLUE}[{Fore.MAGENTA}?{Fore.BLUE}]{Fore.RESET}"
    Information = f"{Fore.MAGENTA}[{Fore.LIGHTMAGENTA_EX}#{Fore.MAGENTA}]{Fore.RESET}"
    Alert = f"{Fore.LIGHTRED_EX}[{Fore.RED}!{Fore.LIGHTRED_EX}]{Fore.RESET}"
class Utils:
    Work_Folder = "WorkFolder"

    def clear_folder(folder_path):

        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)

            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  

def Main():
    System.Clear()
    Utils.clear_folder("WorkFolder")
    Display.ShowTitleScreen()

    print(f"{Display.Information} The file must be in the same folder as {Fore.YELLOW}'main.py'{Fore.RESET}.")
    executable_to_extract_Name = input(f"{Display.Question}{Fore.RESET} Executable to decompile : ")
    
    if executable_to_extract_Name.endswith(".exe"):
        executable_to_extract_Name_ForCheck = Path(executable_to_extract_Name)
        if executable_to_extract_Name_ForCheck.exists():
            current_extraction_folder = ExtractFiles(executable_to_extract_Name)

            System.Title(f"Files of {executable_to_extract_Name}")
            ListFiles(current_extraction_folder)

            FileNameToDecompile = input(f"{Display.Question} Compiled python archive to decompile (*.pyc only) : ")
            FileToDecompile =  current_extraction_folder + "/" + FileNameToDecompile

            if FileToDecompile.endswith(".pyc"):
                run_pylingual(FileToDecompile, current_extraction_folder)
            else:
                print(f"{Display.Alert} This file must be a {Fore.YELLOW}compiled Python file{Fore.RESET} (.pyc)!")
                time.sleep(4)
                Main()
        else:
            print(f"{Display.Alert} File not foud!")
            time.sleep(4)
            Main()
    else:
        print(f"{Display.Alert} This file must be an {Fore.YELLOW}executable{Fore.RESET} (.exe)!")
        time.sleep(4)
        Main()


def ExtractFiles(FilePath):
    LaunchPyinstxtractorCMD = subprocess.run(
        ["pyinstxtractor-ng.exe", FilePath],
        capture_output=True,
        text=True
    )
    CMDoutput = LaunchPyinstxtractorCMD.stdout

    print(CMDoutput)

    CurrentExtractedFolderPath = FilePath + "_extracted"
    
    shutil.move(CurrentExtractedFolderPath, Utils.Work_Folder)
    
    ExtractedFolderPath_with_WorkFolder = Utils.Work_Folder + "/" + CurrentExtractedFolderPath
    System.Clear()
    return ExtractedFolderPath_with_WorkFolder


def ListFiles(folder, depth=0):
    

    indent = "    " * depth

    for item in os.listdir(folder):

        full_path = os.path.join(folder, item)

        icon = "📁"

        if os.path.isdir(full_path):
            print(f"{indent}[{icon}] {item}")
            ListFiles(full_path, depth + 1)  # +1 niveau

        else:
            if item.endswith(".txt"):
                icon = "📄"
            elif item.endswith(".pyc"):
                icon = "⚙️"
            elif item.endswith(".zip"):
                icon = "💼"
            elif item.endswith(".pyd"):
                icon = "🧩"
            elif item.endswith(".pyz"):
                icon = "📦"
            elif item.endswith(".dll"):
                icon = "🪟"

            print(f"{indent}[{icon}] {item}")

    return folder


def run_pylingual(input_path, output_dir):

    System.Clear()
    System.Title(f"Decompiling {input_path}")

    project_dir = Path(__file__).parent.resolve()
    cmd_file = project_dir / "run_pylingual.cmd"

    args = [
        "cmd.exe",
        "/c",
        str(cmd_file),
        str(input_path),
        str(output_dir)
    ]

    subprocess.run(args)

    Show_Code(input_path, output_dir)


def Show_Code(target, file_path):
    HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        html, body, #container {
            width: 100%;
            height: 100%;
            margin: 0;
            overflow: hidden;
        }
    </style>
</head>
<body>
    <div id="container"></div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs/loader.min.js"></script>

    <script>
        require.config({
            paths: {
                vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs'
            }
        });

        require(['vs/editor/editor.main'], function () {

            const editor = monaco.editor.create(document.getElementById('container'), {
                value: __CODE__,
                language: 'python',
                theme: 'vs-dark',
                automaticLayout: true,
                minimap: {
                    enabled: false
                }
            });

        });
    </script>
</body>
</html>
"""
    filename = os.path.basename(target)

    decompiled_target = os.path.join(
        file_path,
        "decompiled_" + filename[:-1]
    )

    with open(decompiled_target, "r", encoding="utf-8") as f:
        code = f.read()

    html = HTML.replace("__CODE__", json.dumps(code))

    webview.create_window(
        title=f"Code of {target}",
        html=html,
        width=1200,
        height=800
    )

    webview.start()
    print(f"{Display.Information} Press Enter to decompile another archive.")
    os.system("pause>nul")
    Main()

Main()