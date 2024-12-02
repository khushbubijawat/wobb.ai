import os

def check_if_file_exists(file_path):
    """Checks if a file exists."""
    return os.path.exists(file_path)

def create_placeholder_file(file_path, content="Placeholder content"):
    """Creates a placeholder file with default content."""
    with open(file_path, "w") as file:
        file.write(content)
