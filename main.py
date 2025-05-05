# -*- coding: utf-8 -*-

import sys, os, subprocess
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher

class SublimeProjectLauncher(FlowLauncher):

    def query(self, query):
        return [
            {
                "Title": "Open Sublime in AllTexts",
                "SubTitle": "Open Sublime Text in D:\\InstalledSoftwares\\Sublime Text\\AllTexts",
                "IcoPath": "sublime.png",
                "JsonRPCAction": {
                    "method": "open_sublime",
                    "parameters": [r"D:\InstalledSoftwares\Sublime Text\AllTexts"]
                }
            },
            {
                "Title": "Open Sublime in Notepad",
                "SubTitle": "Open Sublime Text in D:\\Downloads\\Documents\\Notepad",
                "IcoPath": "sublime.png",
                "JsonRPCAction": {
                    "method": "open_sublime",
                    "parameters": [r"D:\Downloads\Documents\Notepad"]
                }
            }
        ]

    def open_sublime(self, folder_path):
        sublime_path = r"D:\InstalledSoftwares\Sublime Text\sublime_text.exe"
        try:
            subprocess.Popen([sublime_path, folder_path])
        except Exception as e:
            return [{
                "Title": "Error launching Sublime",
                "SubTitle": str(e),
                "IcoPath": "Images/app.png"
            }]

if __name__ == "__main__":
    SublimeProjectLauncher()
