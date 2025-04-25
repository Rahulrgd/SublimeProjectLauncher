import os
import json
from flowlauncher import FlowLauncher

# 💡 Change these to your actual paths
PROJECTS_FILE = "projects.json"  # The file to store projects
SUBLIME_PATH = "D:\\InstalledSoftwares\\Sublime Text\\sublime_text.exe"

class SublimeProjectLauncher(FlowLauncher):
    
    def __init__(self):
        self.load_projects()
        super().__init__()

    def load_projects(self):
        """Load the project list from projects.json"""
        if os.path.exists(PROJECTS_FILE):
            with open(PROJECTS_FILE, 'r') as file:
                data = json.load(file)
                self.projects = data.get("projects", [])
        else:
            self.projects = []
    
    def save_projects(self):
        """Save the project list to projects.json"""
        with open(PROJECTS_FILE, 'w') as file:
            json.dump({"projects": self.projects}, file, indent=4)

    def query(self, query):
        items = []
        if query.lower() == "add":
            items.append({
                "Title": "Add a new project directory",
                "SubTitle": "Enter the full path of the directory",
                "IcoPath": "icon.png",
                "JsonRPCAction": {
                    "method": "add_project",
                    "parameters": [],
                    "dontHideAfterAction": True
                }
            })
        
        elif query.lower() == "remove":
            for project in self.projects:
                items.append({
                    "Title": f"Remove {project}",
                    "SubTitle": "Click to remove from the list",
                    "IcoPath": "icon.png",
                    "JsonRPCAction": {
                        "method": "remove_project",
                        "parameters": [project],
                        "dontHideAfterAction": True
                    }
                })

        else:
            for project in self.projects:
                items.append({
                    "Title": project,
                    "SubTitle": f"Open in Sublime: {project}",
                    "IcoPath": "icon.png",
                    "JsonRPCAction": {
                        "method": "open_in_sublime",
                        "parameters": [project],
                        "dontHideAfterAction": True
                    }
                })
        
        return items or [{
            "Title": "No matching projects found",
            "SubTitle": "Try searching again",
            "IcoPath": "icon.png"
        }]
    
    def open_in_sublime(self, path):
        os.system(f'"{SUBLIME_PATH}" "{path}"')

    def add_project(self, _):
        # You need to handle user input for adding the path, here's an example
        new_project = input("Enter the full path of the project folder: ")
        if os.path.isdir(new_project):
            self.projects.append(new_project)
            self.save_projects()
        else:
            print(f"{new_project} is not a valid directory!")

    def remove_project(self, project):
        """Remove the project directory from the list"""
        if project in self.projects:
            self.projects.remove(project)
            self.save_projects()

if __name__ == "__main__":
    SublimeProjectLauncher()
