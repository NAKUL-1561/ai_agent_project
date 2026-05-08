from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file

available_functions = types.Tool(
    function_declarations=[schema_get_files_info, 
        schema_run_python_file, 
        schema_get_file_content, 
        schema_write_file],
)

def call_function(function_call, verbose=False):
    function_map = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file
    }

    function_name = function_call.name or ""

    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")
    
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    # Make a shallow copy of args and set working_directory
    args = dict(function_call.args) if function_call.args else {}
    args["working_directory"] = "./calculator"
    
    # Call the function and get the result
    function_result = function_map[function_name](**args)
    
    # Return a Content object with the result
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
