def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src_file:
            with open(destination_file, 'w') as dest_file:
                for line in src_file:
                    dest_file.write(line)
        print(f"Contents from '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: One or both files not found.")
    except IOError as e:
        print(f"Error: {e}")


source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

copy_file(source_file, destination_file)
