import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
available_functions = types.Tool(function_declarations=[schema_get_files_info],)


def get_files_info(working_directory, directory="."):
    #workingDIR is the directory you are working out of
    #newJoin is the addition of file_path to the Working Directory
    #fullPath is the Absolute Path of the Working Directory + file_path
    #targetPAth is fullPath converted into it's true form

    workingDIR = os.path.abspath(working_directory)
    newJoin = os.path.join(working_directory, directory)
    fullPath = os.path.abspath(newJoin)
    target_dir = os.path.normpath(os.path.join(workingDIR, directory))
    valid_target_dir = os.path.commonpath([workingDIR, target_dir]) == workingDIR

    # print (f"Working Directory: {working_directory}")
    # print (f"New Directory to add: {directory}")
    # print (f"Absolute Working Directory: {workingDIR}")
    # #Asolute Path of Working Directory
    # print (f"Joined: {fart}")
    # print (f"full Path: {fullPath}")
    # #Absolute Path of Working Directory + New Directory
    # print (f"Target Directory: {target_dir}")
    # #Absolute Path of Working Directory + New Directory in it;s true form

 


    contents = os.listdir(target_dir)
    if not valid_target_dir:
        print (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')


    if not os.path.isdir(target_dir):
        print (f'Error: "{directory}" is not a directory')

        

    # except Exception as e:
    #     error_msg = f"Error: {str(e)}"
    #     print(error_msg)
    #     return error_msg


    
    fileData = []

    for items in contents:
        fileSize = (os.path.getsize(os.path.join(target_dir, items)))
        isDIR = (os.path.isdir(os.path.join(target_dir, items)))
        itemData = (f"- {items}: file_size={fileSize} bytes, is_dir={isDIR}")
        print(itemData)
        fileData.append(itemData)

    endResult = "\n".join(fileData)
    return endResult





