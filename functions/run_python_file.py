import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        absolute_path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(absolute_path, file_path))
        valid_target_file = os.path.commonpath([absolute_path, target_file])
        is_a_file = os.path.isfile(target_file)

        if valid_target_file != absolute_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not is_a_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        
        if args:
            command.extend(args)
        
        result = subprocess.run(
            command,
            cwd=absolute_path,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        output = ""
        
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        
        if not result.stdout and not result.stderr:
            output += "No output produced"
        else:
            if result.stdout:
                output += f"STDOUT:\n{result.stdout}"
            if result.stderr:
                output += f"STDERR:\n{result.stderr}"
        
        return output.rstrip()
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
