import os
import subprocess
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
from flox import Flox

class SublimeProjectLauncher(Flox):
    def query(self, query):
        try:
            results = []
            sublime_path = self.settings.get("sublimeAppPath", "")
            raw_dirs = self.settings.get("projectDirectories", "")
            dirs = [d.strip() for d in raw_dirs.splitlines() if d.strip()]

            if not dirs:
                self.add_item(
                    title="No project folders configured.",
                    subtitle="Please set projectDirectories in plugin settings.",
                    icon="Images/app.png"
                )
                return

            for path in dirs:
                folder_name = os.path.basename(path.rstrip("\\/"))
                self.add_item(
                    title=f"Open {folder_name} in Sublime",
                    subtitle=path,
                    icon="Images/app.png",
                    method="open_in_sublime",
                    parameters=[sublime_path, path]
                )
        except Exception as e:
            self.add_item(
                title="Error loading settings",
                subtitle=str(e),
                icon="Images/app.png"
            )

    def open_in_sublime(self, sublime_path, folder_path):
        try:
            subprocess.Popen([sublime_path, folder_path])
        except Exception as e:
            self.add_item(
                title="Failed to launch Sublime",
                subtitle=str(e),
                icon="Images/app.png"
            )

if __name__ == "__main__":
    SublimeProjectLauncher()
