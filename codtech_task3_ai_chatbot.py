import nltk
import random
import string
import warnings
warnings.filterwarnings("ignore")

from nltk.chat.util import Chat, reflections

# Predefined pairs (pattern, response) for the chatbot
pairs = [
    [
        r"(hi|hello|hey)",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I am a CodTech Chatbot created by Akash."]
    ],
    [
        r"how are you?",
        ["I'm doing great! How can I assist you?"]
    ],
    [
        r"(what can you do|your purpose)",
        ["I can answer basic queries using NLP. Try asking me something!"]
    ],
    [
        r"(bye|exit|quit)",
        ["Goodbye! Have a nice day.", "Bye! See you soon."]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase?"]
    ]
]

# Function to initiate the chatbot
def codtech_chatbot():
    print("CodTech Chatbot: Hello! Type 'bye' to exit.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()
# Run the chatbot
if __name__ == "__main__":
    codtech_chatbot()
