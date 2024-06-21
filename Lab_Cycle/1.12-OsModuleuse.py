import os

def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Error: Directory '{directory_name}' already exists.")
    except OSError as e:
        print(f"Error creating directory '{directory_name}': {e}")

def directory_listing(directory_path):
    try:
        files = os.listdir(directory_path)
        print(f"\nListing files and directories in '{directory_path}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except OSError as e:
        print(f"Error listing directory '{directory_path}': {e}")

def search_py_files(directory_path):
    try:
        print(f"\nSearching for .py files in '{directory_path}':")
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".py"):
                    print(os.path.join(root, file))
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except OSError as e:
        print(f"Error searching files in '{directory_path}': {e}")

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except OSError as e:
        print(f"Error removing file '{file_path}': {e}")

# 
if __name__ == "__main__":
    create_directory("test_directory")
    
    
    directory_listing(".")
    
    
    search_py_files(".")
    
    
    file_to_remove = input("\nEnter the file path to remove: ")
    remove_file(file_to_remove)
