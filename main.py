import argparse
import os
from google import genai
from prompt import system_prompt
from call_function import available_functions
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("prompt", help="The prompt to send to the model")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
user_prompt = args.prompt

messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

if api_key is None:
    raise RuntimeError("environment variable wasn't found")

response = client.models.generate_content(
    model = "gemini-2.5-flash", 
    contents = messages,
    config = types.GenerateContentConfig(
        tools=[available_functions], 
        system_instruction=system_prompt,
    )
)
if response.usage_metadata is None:
    raise RuntimeError("API response missing  usage metadata. Request may have failed.")

prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

if args.verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {prompt_tokens}")
    print(f"Response tokens: {response_tokens}")

if response.function_calls:
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
else:
    print(response.text)
