from transformers import MarianMTModel, MarianTokenizer

# Load model and tokenizer
model_name = "Helsinki-NLP/opus-mt-mul-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Read Malayalam transcription
with open("output_transcription.txt", "r", encoding="utf-8") as f:
    mal_text = f.read()

# Tokenize and translate
inputs = tokenizer([mal_text], return_tensors="pt", padding=True)
translated = model.generate(**inputs)

# Decode English text
english_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]

# Save English translation
with open("translation_output.txt", "w", encoding="utf-8") as f:
    f.write(english_text)

print("✅ Malayalam → English translation saved in translation_output.txt")
print("\n--- Translation ---\n")
print(english_text)
