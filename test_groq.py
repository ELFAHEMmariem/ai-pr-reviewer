
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

response = client.chat.completions.create(
    model=os.getenv(
        "GROQ_MODEL",
        "openai/gpt-oss-120b"
    ),
    messages=[
        {
            "role": "system",
            "content": "You are a code reviewer."
        },
        {
            "role": "user",
            "content": "What is a pull request?"
        }
    ],
    temperature=0,
)

print(response.choices[0].message.content)
