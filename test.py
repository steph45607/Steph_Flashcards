from googletrans import Translator, constants
from pprint import pprint

translator = Translator()
words = ["Kuning", "Biru", "Merah"]
translation = translator.translate(words, dest="es", src="id")
for translation in translation:
    print(f"{translation.origin}({translation.src}) --> {translation.text} ({translation.dest})")
# pprint(constants.LANGUAGES)