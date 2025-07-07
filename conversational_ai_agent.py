# Import the Google Generative AI library
from google import genai
import os
import json
from dotenv import load_dotenv
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

# API key for Gemini from environment variables
api_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key, temperature=0.7)

# List to store conversation history (memory) for context across interactions
memory = ConversationBufferMemory(return_messages=True)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)


# Optional: Load existing memory from file
def load_memory():
    if os.path.exists("memory_store.json"):
        with open("memory_store.json", "r") as f:
            mem = json.load(f)
            for m in mem:
                memory.chat_memory.add_user_message(m['user'])
                memory.chat_memory.add_ai_message(m['ai'])

# Optional: Save memory to file
def save_memory():
    history = []
    for m in memory.chat_memory.messages:
        if m.type == "human":
            history.append({"user": m.content, "ai": ""})
        elif m.type == "ai" and len(history) > 0:
            history[-1]["ai"] = m.content
    with open("memory_store.json", "w") as f:
        json.dump(history, f, indent=2)


# Main chat function with command-line interface
def chat():
    # Welcome message
    print("Hello, how can I help you?")
    print("Type exit to quit")
    load_memory()

    # Conversation loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            save_memory()
            print("Goodbye! 👋")
            break
        response = conversation.predict(input=user_input)
        print("Gemini:", response)


# Direct execution of the chat function (will always run when file is executed)
chat()