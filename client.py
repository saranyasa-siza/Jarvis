import os
from dotenv import load_dotenv  # type: ignore
import google.genai as genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Write a one-sentence bedtime story about a unicorn."
)

print(response.text)