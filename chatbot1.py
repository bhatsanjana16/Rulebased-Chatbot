import re
import random

patterns_responses = [
    [r"my name is (.*)", ["Hello %1! How can I assist you today?", "Nice to meet you, %1! How's your day going?"]],
    [r"hi|hey|hello", ["Hello, how can I help you today?", "Hey there! What can I do for you?", "Hi! What would you like to talk about today?"]],
    [r"what is your name?", ["I am Daisy, your helpful assistant. What's your name?", "You can call me Daisy, what can I assist you with?"]],
    [r"how are you?", ["I'm just a bot, but I'm doing well! How about you?", "I don't have feelings, but thanks for asking! How are you doing?"]],
    [r"i am feeling (.*)", ["That's great to hear! How can I assist you further?", "I'm glad you're feeling %1! What would you like to talk about?"]],
    [r"can you help me with (.*)", ["Of course, I can help you with %1. Can you provide me with more details?", "I'd be happy to assist you with %1. What specifically would you like help with?"]],
    [r"sorry (.*)", ["No worries! How can I assist you?", "It's alright. Let's focus on your query. How can I help?"]],
    [r"thank you|thanks", ["You're welcome!", "No problem at all!", "Happy to help! What else can I assist you with?"]],
    [r"quit", ["Goodbye! Have a wonderful day!", "Bye! Hope to chat with you again soon!"]],
    [r"(.*)", ["I'm sorry, I didn't catch that. Could you rephrase?", "Hmm, I'm not sure I understand. Could you elaborate?"]]
]

default_response = "I'm sorry, I don't understand that. Can you please rephrase?"

# def get_response(user_input):
#     for pattern, responses in patterns_responses:
#         match = re.search(pattern, user_input, re.IGNORECASE)
#         if match:
#             response = random.choice(responses)
#             if "%1" in response and match.groups():
#                 response = response.replace("%1", match.group(1))
#             return response
#     return default_response

def get_response(user_input):
    # Iterate through the defined patterns and their responses
    for pattern, responses in patterns_responses:
        # Attempt to match the user input against the current pattern
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            # Choose a random response from the matched responses
            response = random.choice(responses)
            # Check if there are any capturing groups in the match
            if match.groups():
                # Use the first capturing group to replace the placeholder in the response
                response = response.replace("{feeling}", match.group(1))  # Changed placeholder to {feeling}
            return response
    # Return a default response if no patterns matched
    return default_response

def Daisy():
    print("Daisy: Hi! I am your rule-based chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if re.search(r'bye|goodbye', user_input, re.IGNORECASE):
            print("Daisy: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Daisy: {response}")

def main():
    Daisy()

main()
