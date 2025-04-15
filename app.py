import subprocess
from collections import defaultdict

class RenameGitFolder:
    def __init__(self, old_folder_name, new_folder_name):
        self.old_folder_name = old_folder_name
        self.new_folder_name = new_folder_name
        self.folders = defaultdict(set)

    def ListFoldersOnThisRepository(self):
        try:
            result = subprocess.run(['git', 'ls-tree', '-r', '--name-only', 'HEAD'], capture_output=True, text=True, check=True)
            files = result.stdout.splitlines()

            # Clear previous folder data
            self.folders.clear()

            for file in files:
                parts = file.split('/')
                if len(parts) > 1:
                    folder = parts[0]
                    subfolder = '/'.join(parts[1:])
                    self.folders[folder].add(subfolder)

            # Show folders and subfolders
            if self.folders:
                print("Folders and their subfolders:")
                for folder, subfolders in sorted(self.folders.items()):
                    print(f"Folder: {folder}")
                    for subfolder in sorted(subfolders):
                        print(f"  - Subfolder: {subfolder}")
            else:
                print("No folders found in the Git repository.")

        except subprocess.CalledProcessError as e:
            print(f"Error running git ls-tree: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def RenameOldFolder(self):
        try:
            print("Renaming Folder......")
            subprocess.run(['git', 'mv', self.old_folder_name, self.new_folder_name], check=True)
            print("Folder Renamed......")
        except subprocess.CalledProcessError as e:
            print(f"Error running git mv command: {e}")

    def RenameSubfolder(self, folder_name, old_subfolder_name, new_subfolder_name):
        try:
            if folder_name in self.folders and old_subfolder_name in self.folders[folder_name]:
                # Construct full paths for renaming
                old_path = f"{folder_name}/{old_subfolder_name}"
                new_path = f"{folder_name}/{new_subfolder_name}"
                
                print(f"Renaming Subfolder '{old_subfolder_name}' to '{new_subfolder_name}' in folder '{folder_name}'...")
                subprocess.run(['git', 'mv', old_path, new_path], check=True)
                print(f"Subfolder '{old_subfolder_name}' renamed to '{new_subfolder_name}'.")
                # Update the in-memory folders dictionary
                self.folders[folder_name].remove(old_subfolder_name)
                self.folders[folder_name].add(new_subfolder_name)
            else:
                print(f"Subfolder '{old_subfolder_name}' not found in folder '{folder_name}'.")
        except subprocess.CalledProcessError as e:
            print(f"Error running git mv command: {e}")

    def GitAdd(self):
        try:
            print("Git Add......")
            subprocess.run(['git', 'add', '.'], check=True)
            print("Git Add Completed......")
        except subprocess.CalledProcessError as e:
            print(f"Error running git Add command: {e}")

    def GitCommited(self, message):
        try:
            print("Git Commit......")
            subprocess.run(['git', 'commit', '-m', message], check=True)
            print("Git Commit Completed......")
        except subprocess.CalledProcessError as e:
            print(f"Error running Commit command: {e}")

    def Push(self):
        try:
            print("Git Push......")
            subprocess.run(['git', 'push', 'origin'], check=True)
            print("Git Push Completed......")
        except subprocess.CalledProcessError as e:
            print(f"Error running Push command: {e}")

# Example Usage
if __name__ == "__main__":
    r = RenameGitFolder("visual", "visualww")
    r.ListFoldersOnThisRepository()  # List the folders
    r.RenameOldFolder()               # Rename the specified main folder
    r.GitAdd()                        # Stage the changes
    r.GitCommited("Renamed visual to visualww")  # Commit the changes
    r.Push()                          # Push to remote

    # If you want to rename a subfolder as well:
    r.RenameSubfolder("visualww", "subfolder", "s")