# -*- coding: utf-8 -*-

import sys, os, subprocess
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher


class SublimeProjectLauncher(FlowLauncher):

    def __init__(self):
        super().__init__()

    def query(self, query):
        try:
            results = self.get_project_directory_results()
            if isinstance(results, list) and all(isinstance(item, dict) for item in results):
                return results
        except Exception as e:
            return [{
                "Title": "Error loading settings",
                "SubTitle": str(e),
                "IcoPath": "sublime.png"
            }]
        return []

    def get_project_directory_results(self):
        results = []

        # Safe defaults
        default_sublime_path = r"D:\InstalledSoftwares\Sublime Text\sublime_text.exe"
        default_dirs = []

        # Load settings with fallback
        sublime_path = self.settings.get("sublimeAppPath", default_sublime_path)
        raw_dirs = self.settings.get("projectDirectories", "")

        if isinstance(raw_dirs, str):
            project_dirs = [d.strip() for d in raw_dirs.splitlines() if d.strip()]
        elif isinstance(raw_dirs, list):  # Also handle if user provides list
            project_dirs = [d.strip() for d in raw_dirs if isinstance(d, str) and d.strip()]
        else:
            project_dirs = default_dirs

        for path in project_dirs:
            folder_name = os.path.basename(path.rstrip("\\/"))
            results.append({
                "Title": f"Open Sublime in {folder_name}",
                "SubTitle": f"Open Sublime Text in {path}",
                "IcoPath": "sublime.png",
                "JsonRPCAction": {
                    "method": "open_sublime",
                    "parameters": [path],
                    "dontHideAfterAction": False
                }
            })

        if not results:
            results.append({
                "Title": "No project directories found.",
                "SubTitle": "Please set them in the plugin settings.",
                "IcoPath": "sublime.png"
            })

        return results

    def open_sublime(self, folder_path):
        sublime_path = self.settings.get("sublimeAppPath", r"D:\InstalledSoftwares\Sublime Text\sublime_text.exe")
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
