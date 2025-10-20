from deep_translator import GoogleTranslator
from langdetect import detect
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/process_text")
async def process_text(data: TextInput):
    text = data.text.strip()
    if not text:
        return {"error": "Empty text"}

    try:
        lang = detect(text)
    except Exception:
        lang = "unknown"

    # ✅ Translate Malayalam → English
    if lang == "ml":
        try:
            translated_text = GoogleTranslator(source='ml', target='en').translate(text)
        except Exception as e:
            print("Translation failed:", e)
            translated_text = text
    else:
        translated_text = text

    legal_mapping_info = "Legal analysis will be generated based on the translated content."

    return {
        "detected_language": lang,
        "original_text": text,
        "translated_text": translated_text,
        "legal_mapping": legal_mapping_info
    }
