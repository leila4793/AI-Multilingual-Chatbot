from googletrans import Translator

translator = Translator()

def detect_language(text):
    return translator.detect(text).lang

def translate_text(text, src_lang, dest_lang):
    return translator.translate(text, src=src_lang, dest=dest_lang).text
