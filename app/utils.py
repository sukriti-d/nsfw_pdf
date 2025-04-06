import re

NSFW_KEYWORDS = [
    "damn", "shit", "fuck", "idiot", "bitch", "bastard", "asshole",
    "dumb", "crap", "bullshit", "slut", "whore", "freak", "moron"
]

def contains_nsfw_keywords(text: str) -> bool:
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in NSFW_KEYWORDS) + r')\b', re.IGNORECASE)
    return bool(pattern.search(text))

def highlight_nsfw_keywords(text: str) -> str:
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in NSFW_KEYWORDS) + r')\b', re.IGNORECASE)
    return pattern.sub(r'***\1***', text)

def clean_nsfw_keywords(text: str) -> str:
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in NSFW_KEYWORDS) + r')\b', re.IGNORECASE)
    return pattern.sub("[censored]", text)
