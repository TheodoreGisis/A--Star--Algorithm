import subprocess

def list_git_folders():
    try:
        result = subprocess.run(['git', 'ls-tree', '-r', '--name-only', 'HEAD'], capture_output=True, text=True, check=True)       
        
        files = result.stdout.splitlines()
        folders = set()

        for file in files:
            folder = '/'.join(file.split('/')[:-1])  
            if folder:  
                folders.add(folder)

        if folders:
            print("Git folders:")
            for folder in sorted(folders):
                print(f"- {folder}")
        else:
            print("No folders found in the Git repository.")

        return folders

    except subprocess.CalledProcessError as e:
        print(f"Error running git ls-tree: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def rename_folder():
    old_folder_name = "Visualize"
    new_folder_name = "test122"

    try:
        naming_command = subprocess.run(['git' , 'mv' , old_folder_name , new_folder_name])
        commit_message("Change folder name")

    except subprocess.CalledProcessError as e:
        print(f"Error running git mv command: {e}")

def git_add():
    naming_command = subprocess.run(['git' , 'add' , '.' ])
    


def commit_message(message):
    commiting_result = subprocess.run(['git' , 'commit' , '-m', message])

def push():
    commiting_result = subprocess.run(['git' , 'push' , 'origin'])

if __name__ == "__main__":
    list_git_folders()
    # rename_folder()
    # git_add()
    push()