import os
MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    workingDIR = os.path.abspath(working_directory)   
    #The Directory you are working out of
    newJoin = os.path.join(working_directory, file_path)
    #adding the *new* directory to Working Directory
    fullPath = os.path.abspath(newJoin)
    #getting the Absolute Path of the Working Directory + New Directory
    targetPath = os.path.normpath(os.path.join(workingDIR, file_path))
    #Converting everything into it's true form
    valid_target_file = os.path.commonpath([workingDIR, targetPath]) == workingDIR

    print (f"Working Directory: {working_directory}")
    print (f"New File Path to add: {file_path}")
    print (f"Absolute Working Directory: {workingDIR}")
    #Asolute Path of Working Directory
    print (f"Joined: {newJoin}")
    print (f"full Path: {fullPath}")
    #Absolute Path of Working Directory + New Directory
    print (f"Target Path: {targetPath}")
    #Absolute Path of Working Directory + New Directory in it;s true form

    if not valid_target_file:
        print (f'Error: Cannot read "{fullPath}" as it is outside the permitted working directory')
        return (f'Error: Cannot read "{fullPath}" as it is outside the permitted working directory')

    if not os.path.isfile(fullPath):
        print (f'Error: File not found or is not a regular file: "{fullPath}"')
        return (f'Error: File not found or is not a regular file: "{fullPath}"')

    print (f'Listing file path: "{fullPath}"\n')
    
    with open(targetPath, "r") as file:
        content = file.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        if file.read(1):
            content += f'[...File "{fullPath}" truncated at {MAX_CHARS} characters]'
        print(content)
    return content

#print(get_file_content('../calculator', 'lorem.txt'))