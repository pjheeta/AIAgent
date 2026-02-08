import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="We'll give our agent the ability to write and overwrite the contents of a specific file in a specified directory relative to the working directory.  All within strict limits",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
            
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The name of the file_path that we will be using",
            ),
            
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content we want to write",
            ),
        },
    ),
)


def write_file(working_directory, file_path, content):
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
        return (f'Error: Cannot write to "{targetPath}" as it is outside the permitted working directory')
   
    if os.path.isdir(fullPath):
        return (f'Error: Cannot write to " {fullPath}" as it is a directory')

    if not os.path.isdir(os.path.dirname(fullPath)):
         print (f'Error: fullPath "{os.path.dirname(fullPath)}" is NOT a directory')
    
    os.makedirs(os.path.dirname(fullPath), exist_ok=True)
    with open(targetPath, "w") as file:
        file.write(content)
    return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    

#print (write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))







    # with open(targetPath, "r") as file:
    #     content = file.read(MAX_CHARS)
    #     # After reading the first MAX_CHARS...
    #     if file.read(1):
    #         content += f'[...File "{fullPath}" truncated at {MAX_CHARS} characters]'
    #     print(content)