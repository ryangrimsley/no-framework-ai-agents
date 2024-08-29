import os

def save_to_file(content: str, file_name: str):
    """
    Save some content to a file when passing in the content and the name to name the file. 
    Do not pass in a file extension when passing in the file name. 

    Parameters:
    content(str): The content to save to a file
    file_name(str): The name to name the file
    """
    file_name = f"{file_name}.txt"
    root_path = os.path.dirname(os.path.dirname(file_name))
    file_path = os.path.join(root_path, file_name)
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Content successfully written to {file_name}.")
    except Exception as e:
        print(f"An error occurred while writing to {file_name}: {e}")