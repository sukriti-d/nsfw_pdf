def rewrite_text(text: str) -> str:
    replacements = {
        "bullshit": "nonsense",
        "damn": "darn",
        "bastard": "person",
        "fuck": "mess",
        "shit": "trouble",
        "idiot": "individual",
        "moron": "person",
        "asshole": "individual",
        "slut": "person",
        "dumb": "uninformed",
    }
    for word, replacement in replacements.items():
        text = text.replace(word, replacement).replace(word.capitalize(), replacement.capitalize())
    return text
