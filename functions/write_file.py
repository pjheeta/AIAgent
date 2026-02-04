import os

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
    
    #check print statements
    # print (f"Working Directory: {working_directory}")       
    # print (f"file_path: {os.path.dirname(file_path)}")
    # print (f"Working Directory: {working_directory}")
    # print (f"New File Path to add: {file_path}")
    # print (f"Absolute Working Directory: {workingDIR}")
    # print (f"Joined: {newJoin}")
    # print (f"full Path: {fullPath}")
    # print (f"Target Path: {targetPath}")

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