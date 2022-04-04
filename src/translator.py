#!/usr/bin/python3
from deep_translator import GoogleTranslator

# input source_lang, target_lang in format 'en', 'ru' etc.
# output -> translated text
def getTranslation(source_text, source_lang, target_lang):
    text = source_text
    translated = GoogleTranslator(source=(source_lang.lower()), target=(
        target_lang.lower())).translate(text=text)
    return translated



strTransl = '''Ticking away the moments that make up a dull day
Fritter and waste the hours in an offhand way
Kicking around on a piece of ground in your hometown
Waiting for someone or something to show you the way'''
print(getTranslation(strTransl, 'en', 'ru'))