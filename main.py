# To use this script, install the Google Generative AI package:
# pip install google-genai

from google import genai

# gemini api key
GEMINI_API_KEY="AIzaSyDUTio2GvIrncmWcWll6h1uEbK3r5ybnx4"

# Create a client
client = genai.Client(api_key=GEMINI_API_KEY)

#function to get data from the generative ai llm model
def get_data(input):
    response_ai = client.models.generate_content(
        model="gemini-2.5-flash",  #model name
        contents=[input]           #passing the input to the ai modal
    )
    return response_ai.text #returning the response received from ai modal to the call

#function to start a chat
def chat():
    print("Hello, how can I help you?")
    print("Type exit to quit")

#infinite loop till the user enters exit
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = get_data(user_input) #function call to get data from api
        print("Gemini:",response)

chat()
