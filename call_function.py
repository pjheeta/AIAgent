from google.genai import types
#from functions.get_files_info import schema_get_files_info
from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *

# Debug prints
# print(f"schema_get_files_info exists: {schema_get_files_info}")
# print(f"schema_get_file_content exists: {schema_get_file_content}")

available_functions = types.Tool(function_declarations=[
    schema_get_files_info,
    schema_get_file_content,
    schema_write_file,
    schema_run_python_file,
    ])

