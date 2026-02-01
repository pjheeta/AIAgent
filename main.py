import os
import argparse
from google import genai
from dotenv import load_dotenv
from google.genai import types


print("load_dotenv()") 
load_dotenv("api.env")
api_key = os.environ.get("GEMINI_API_KEY")


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


    response = client.models.generate_content(model='gemini-2.5-flash', contents=messages)

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)
   

if __name__ == "__main__":
    main()
