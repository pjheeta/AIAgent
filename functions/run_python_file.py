import os
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
        return (f'Error: Cannot write to "{targetPath}" as it is outside the permitted working directory')
    
    if not os.path.isfile(fullPath):
        print (f'Error: File not found or is not a regular file: "{fullPath}"')

    if not file_path.endswith("py"):
        print (f'Error: "{file_path}" is not a Python file')



    command = ["python", fullPath]
# print ({run_python_file("calculator", "lorem.py")})
