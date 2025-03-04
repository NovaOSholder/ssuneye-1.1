import json
import random
import nltk
from textblob import TextBlob

nltk.download('punkt')

FILE_NAME = "memoryCache32.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return data
    except:
        return {}

def save_data(question, answer):
    data = load_data()
    data[question] = answer

    with open(FILE_NAME, "w") as file:
        json.dump(data, file)

def sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        return "You seem happy! 😊"
    elif sentiment_score < 0:
        return "You seem sad. Can I help? 😞"
    else:
        return "You seem neutral. 🤔"

def find_best_answer(user_input, data):
    if not data:
        return "I haven't learned much yet, you can teach me by asking questions!"

    for question in data.keys():
        if question.lower() in user_input.lower() or user_input.lower() in question.lower():
            return data[question]

    return "I don't know about this topic. If you tell me the right answer, I can learn!"

print("Chatbot: Hello! You can teach me something. Type 'exit' to quit.")

data = load_data()

if not data:
    data = {
        "Hello": "Hello, how are you?",
        "What's your name?": "I am a chatbot.",
        "How are you?": "I don't have feelings since I'm an AI, but talking to you is very enjoyable!",
        "Are you good?": "I'm always good, how about you?"
    }

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: See you later! 👋")
        break

    sentiment_response = sentiment_analysis(user_input)
    response = find_best_answer(user_input, data)

    print(f"Chatbot: {sentiment_response} Also, {response}")

    if "I don't know" in response:
        new_answer = input("You tell me, how should I answer this? ")
        save_data(user_input, new_answer)
        print("Chatbot: Thanks! Now I know this. 😊, Reopen the AI and I will answer correctly!")