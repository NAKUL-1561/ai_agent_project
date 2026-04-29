import os

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
