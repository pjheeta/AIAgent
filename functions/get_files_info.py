import os

def get_files_info(working_directory, directory="."):

    workingDIR = os.path.abspath(working_directory)
    #The Directory you are working out of
    newJoin = os.path.join(working_directory, directory)
    #adding the *new* directory to Working Directory
    fullPath = os.path.abspath(newJoin)
    #getting the Absolute Path of the Working Directory + New Directory
    target_dir = os.path.normpath(os.path.join(workingDIR, directory))
    #Converting everything into it's true form

    # print (f"Working Directory: {working_directory}")
    # print (f"New Directory to add: {directory}")
    # print (f"Absolute Working Directory: {workingDIR}")
    # #Asolute Path of Working Directory
    # print (f"Joined: {fart}")
    # print (f"full Path: {fullPath}")
    # #Absolute Path of Working Directory + New Directory
    # print (f"Target Directory: {target_dir}")
    # #Absolute Path of Working Directory + New Directory in it;s true form

    valid_target_dir = os.path.commonpath([workingDIR, target_dir]) == workingDIR
    #Checking to see if target_dir is inside workingDIR
    #print (f"Valid Target Directory: {valid_target_dir}")   

    # if valid_target_dir==False:
    #     return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')  

    # if not os.path.isdir(target_dir):
    #     return (f'Error: "{directory}" is not a directory')
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





