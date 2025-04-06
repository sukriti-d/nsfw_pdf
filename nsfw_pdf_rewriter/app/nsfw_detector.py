from transformers import pipeline
from app.utils import contains_nsfw_keywords

classifier = pipeline("text-classification", model="facebook/roberta-hate-speech-dynabench-r4-target")

def is_text_nsfw(text: str) -> bool:
    if contains_nsfw_keywords(text):
        return True

    chunks = [text[i:i+512] for i in range(0, len(text), 512)]
    for chunk in chunks:
        result = classifier(chunk)[0]
        if result["label"].lower() in ["toxic", "hate", "offensive"] and result["score"] > 0.7:
            return True
    return False
