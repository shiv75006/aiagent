# Simple AI agent using Gemini API
# pip install google-genai python-dotenv
from google import genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API key for Gemini from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# Get response from Gemini API
def get_data(input):
    response_ai = client.models.generate_content(
        model="gemini-2.5-flash",  # Model optimized for speed
        contents=[input]           # User input
    )
    return response_ai.text

# Main chat function with command-line interface
def chat():
    print("Hello, how can I help you?")
    print("Type exit to quit")

    # Conversation loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = get_data(user_input)
        print("Gemini:", response)

chat()
