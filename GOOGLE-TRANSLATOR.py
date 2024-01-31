from deep_translator import GoogleTranslator

t = GoogleTranslator(
    source = "auto",
    level = "en"
)

r = t.translate("kaise ho ?")

print(r)