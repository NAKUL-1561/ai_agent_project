import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."


if api_key is None:
    raise RuntimeError("environment variable wasn't found")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=user_prompt
)
if response.usage_metadata is None:
    raise RuntimeError("API response missing  usage metadata. Request may have failed.")

prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count

print(f"User Prompt: {user_prompt}")
print(f"Prompt tokens: {prompt_tokens}")
print(f"Response tokens: {response_tokens}")
print("Response")
print(response.text)