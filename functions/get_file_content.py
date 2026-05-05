import os
from google.genai import types
 
MAX_CHARS = 10000

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file relative to the working directory, with a maximum of 10000 characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="Absolute or relative path to the working directory for file access",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file to read from the working directory",
            ),
        },
        required=["working_directory", "file_path"],
    ),
)

def get_file_content(working_directory, file_path):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_file = os.path.commonpath([absolute_path, target_file])

        if valid_target_file != absolute_path:
            return f'Error: Cannot access "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1):
                file_content_string += f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            return file_content_string
    
    except Exception as e:
        return f"Error: {str(e)}"
