import spacy
from src.language_support import detect_language, translate_text

class Chatbot:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def respond(self, user_input, lang="en"):
        translated_input = translate_text(user_input, lang, "en")
        response = f"Processing: {translated_input}"
        return translate_text(response, "en", lang)

    def run(self):
        print("Chatbot is running. Type 'exit' to stop.")
        while True:
            user_input = input("> ")
            if user_input.lower() == "exit":
                break
            lang = detect_language(user_input)
            print(self.respond(user_input, lang))
