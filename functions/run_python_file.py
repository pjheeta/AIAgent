import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute Python files with optional arguments  in a specified directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file to read.",
            ),
        },
    ),
)

def run_python_file(working_directory, file_path, args=None):
    #workingDIR is the directory you are working out of
    #newJoin is the addition of file_path to the Working Directory
    #fullPath is the Absolute Path of the Working Directory + file_path
    #targetPAth is fullPath converted into it's true form
    
    workingDIR = os.path.abspath(working_directory)   
    newJoin = os.path.join(working_directory, file_path)
    fullPath = os.path.abspath(newJoin)
    targetPath = os.path.normpath(os.path.join(workingDIR, file_path))   
    valid_target_file = os.path.commonpath([workingDIR, targetPath]) == workingDIR

    if not valid_target_file:
        return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile(fullPath):
        return (f'Error: "{file_path}" does not exist or is not a regular file')

    if not file_path.endswith(".py"):
        return (f'Error: "{file_path}" is not a Python file')

    try:    

        command = ["python", fullPath]

    
        if args:  # Check if args were provided (not None and not empty)
            command.extend(args)


        result = subprocess.run(
            command,
            cwd=workingDIR,   #cwd = wurrent working directory
            capture_output=True,
            text=True,
            timeout=30
        )        
        return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"

    except Exception as e:
        return f"Error: executing Python file: {e}"
