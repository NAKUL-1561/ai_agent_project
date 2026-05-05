import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file relative to the working directory, creating the file if it does not exist",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="Absolute or relative path to the working directory where the file should be created or modified",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file to write in the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file",
            ),
        },
        required=["working_directory", "file_path", "content"],
    ),
)

def write_file(working_directory, file_path, content):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_file = os.path.commonpath([absolute_path, target_file])
        is_a_dir = os.path.isdir(target_file)
        parent_directory = os.path.dirname(target_file)
        os.makedirs(parent_directory, exist_ok=True)
        
        if valid_target_file != absolute_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if valid_target_file == is_a_dir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f"Error: {str(e)}"
