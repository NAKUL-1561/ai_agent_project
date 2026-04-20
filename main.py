import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if api_key is None:
    raise RuntimeError("environment variable wasn't found")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)
print(response.text)