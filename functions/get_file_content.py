import os

from config import MAX_FILE_LENGTH


def get_file_content(working_directory: str, file_path: str) -> str | None:
    abs_working_dir = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_file, "r") as f:
            content = f.read()
            if len(content) > MAX_FILE_LENGTH:
                content = (
                    content[:MAX_FILE_LENGTH]
                    + f'[...File "{file_path}" truncated at {MAX_FILE_LENGTH} characters.]'
                )
            return content
    except Exception as e:
        return f"Error reading file: {e}"
