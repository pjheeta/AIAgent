import os
import argparse
from google import genai
from dotenv import load_dotenv
from google.genai import types
from google.genai.types import FunctionCall
from prompts import system_prompt
from call_function import *
from functions.get_files_info import *
from functions.get_file_content import *
from functions.write_file import *
from functions.run_python_file import *

load_dotenv("api.env")
api_key = os.environ.get("GEMINI_API_KEY")
print(f"DEBUG: Number of functions available: {len(available_functions.function_declarations)}")
for func in available_functions.function_declarations:
    print(f"  - {func.name}")


def main():
    print("Hello from aiagent!")
    client = genai.Client(api_key=api_key)
    
    if api_key == None:
        print("API key not found. Please set the GEMINI_API_KEY environment variable.") 
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()


    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
        )

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(response.text)

    if response.function_calls:
        function_results = []  # Track results
        
        for function_call in response.function_calls:
            # Call the function
            function_call_result = call_function(function_call, verbose=args.verbose)
            
            # Verify we got a valid response
            if not function_call_result.parts:
                raise Exception("Function call returned no parts")
            
            if function_call_result.parts[0].function_response is None:
                raise Exception("Function response is None")
            
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("Function response.response is None")
            
            # Add to results
            function_results.append(function_call_result.parts[0])
            
            # Print result if verbose
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        print(f"No function calls, Here is the response in text {response.text}")



if __name__ == "__main__":
    main()
