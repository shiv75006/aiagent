# Import the Google Generative AI library
from google import genai

# API key for Gemini (in production, use environment variables instead)
GEMINI_API_KEY=""

# Initialize the Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

# List to store conversation history (memory) for context across interactions
memory = []

# Get AI response based on conversation history
def get_data(input):
    # Format conversation history for the Gemini API
    content=[]

    # Convert memory to Gemini API format
    for msg in memory:
        if msg["role"] == "user":
            content.append({"role": "user", "parts": [{"text": msg["content"][0]}]})
        elif msg["role"] == "model":
            content.append({"role": "model", "parts": [{"text": msg["content"][0]}]})

    # Send conversation to Gemini API
    response_ai = client.models.generate_content(
        model="gemini-2.5-flash",  # Optimized for speed
        contents=content         # Complete conversation history for context
    )

    # Store AI response in memory
    memory.append({"role":"model","content":[response_ai.text]})

    # Debugging (uncomment if needed)
    # print('\n')
    # print("Chat Memory:",memory)

    return response_ai.text

# Main chat function with command-line interface
def chat():
    # Welcome message
    print("Hello, how can I help you?")
    print("Type exit to quit")

    # Conversation loop
    while True:
        print("\n")  # Newline for formatting
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == "exit":
            break

        # Add user input to conversation memory
        memory.append({"role":"user","content":[user_input]})

        # Get and display AI response
        response = get_data(user_input)
        print("\n")  # Newline for formatting
        print("Gemini:", response)

# Commented code for making this file importable as a module
# if __name__ == "__main__":
#     chat()

# Direct execution of chat function (will always run when file is executed)
chat()
