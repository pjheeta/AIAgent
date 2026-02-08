import os
#from config import *
from google.genai import types
MAX_CHARS = 10000

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the contents of a specific file in a specified directory relative to the working directory, returning the information as a string",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory)",
            ),
             "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path of the file to read.",
            ),
        }
    ),
)

def get_file_content(working_directory, file_path):
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
        print (f'Error: Cannot read "{fullPath}" as it is outside the permitted working directory')

    if not os.path.isfile(fullPath):
        print (f'Error: File not found or is not a regular file: "{fullPath}"')

    print (f'Listing file path: "{fullPath}"\n')
    
    with open(targetPath, "r") as file:
        content = file.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        if file.read(1):
            content += f'[...File "{fullPath}" truncated at {MAX_CHARS} characters]'
        print(content)
    return content

#print(get_file_content('../calculator', 'lorem.txt'))