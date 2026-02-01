import os
from google import genai
from dotenv import load_dotenv

print("load_dotenv()") 
load_dotenv("api.env")
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    print("Hello from aiagent!")
    client = genai.Client(api_key=api_key)
    
    if api_key == None:
        print("API key not found. Please set the GEMINI_API_KEY environment variable.") 
    
    
    response = client.models.generate_content(
    model='gemini-2.5-flash', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )   
    print(response.text)
   

if __name__ == "__main__":
    main()
