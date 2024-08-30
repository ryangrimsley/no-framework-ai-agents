import os

def remove_files_except(script_name, keep_file):
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Iterate over all files in the directory
    for filename in os.listdir(current_dir):
        # Construct full file path
        file_path = os.path.join(current_dir, filename)
        
        # Check if it's a file and not the script itself or README.md
        if os.path.isfile(file_path) and filename not in [script_name, keep_file]:
            os.remove(file_path)
            print(f'Removed: {filename}')
        else:
            print(f'Skipped: {filename}')

if __name__ == "__main__":
    # Get the name of the script itself
    script_name = os.path.basename(__file__)
    
    # Define the file to keep along with the script
    keep_file = 'README.md'
    
    # Call the function
    remove_files_except(script_name, keep_file)
