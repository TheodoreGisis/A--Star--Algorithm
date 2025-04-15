import subprocess
from time import sleep

class RenameGitFolder():

    def __init__(self,OldFolderName,NewFolderName):
        
        self.OldFolderName = OldFolderName
        self.NewFolderName = NewFolderName
        self.folders       = set()

    def ListFoldersOnThisRepository(self):
        try:
            result = subprocess.run(['git', 'ls-tree', '-r', '--name-only', 'HEAD'], capture_output=True, text=True, check=True)       
            
            files = result.stdout.splitlines()

            for file in files:
                folder = '/'.join(file.split('/')[:-1])  
                if folder:  
                    self.folders.add(folder)

            if self.folders:
                print("Git folders:")
                for folder in sorted(self.folders):
                    print(f"- {folder}")
            else:
                print("No folders found in the Git repository.")

            return self.folders

        except subprocess.CalledProcessError as e:
            print(f"Error running git ls-tree: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
       
    def RenameOldFolder(self):
        try:
            print("Renaming Folder......")
            Git_Naming_Command = subprocess.run(['git' , 'mv' , self.OldFolderName , self.NewFolderName])
            print("Folder Renamed......")
        except subprocess.CalledProcessError as e:
            print(f"Error running git mv command: {e}")

    def GitAdd(self):
        try:
            print("Git Add......")
            Git_Add_Command = subprocess.run(['git' , 'add' , '.' ])

            print("Git Add Completed......")
        except subprocess.CalledProcessError as e:
            print(f"Error running git Add command: {e}")

    def GitCommited(self,message):
        try:
            print("Git Commit......")
            Git_Commit_Command = subprocess.run(['git' , 'commit' , '-m', message])

            print("Git Commit Completed......")
        except subprocess.CalledProcessError as e:
            print(f"Error running Commit command: {e}")

    def Push(self):
        try:
            print("Git Push......")
            Git_Commit_Command = subprocess.run(['git' , 'push' , 'origin'])
 
            print("Git Push Completed......")
        except subprocess.CalledProcessError as e:
            print(f"Error running Push command: {e}")


if __name__ == "__main__":
    r = RenameGitFolder("test","visual")
    r.ListFoldersOnThisRepository()
    r.RenameOldFolder()
    r.GitAdd()
    r.GitCommited("test")
