import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure OpenAI client to use Ollama's OpenAI-compatible endpoint
client = OpenAI(
    api_key="ollama",
    base_url="http://192.168.68.104:11434/v1"
)

# Query
query = "Zein da adimen artifizialaren arauketaren arazo nagusiena?"

print(f"Sending request to Ollama server at {client.base_url}...")
print(f"Query: {query}")

try:
    # Create a chat completion using the new OpenAI API
    stream = client.chat.completions.create(
        model="xabi/llama3-eus",
        messages=[
            {"role": "user", "content": query}
        ],
        stream=True
    )
    
    print("\nModel response:")
    
    # Process the streaming response
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end='', flush=True)
    
    print("\n\nResponse complete.")
except Exception as e:
    print(f"Exception occurred: {e}")
    print("\nMake sure your Ollama server is running at:")
    print("http://192.168.68.104:11434")
