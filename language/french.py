"""French Language"""

character_map = {
    "ch": "\u0283",
    "tt": "t",
    "ll": "l",
    "hu": "\u0265",
    "eau": "o",
    "ai": "\u025b",
    "ou": "u",
    "om": "\u0254\u0303",
    "an": "\u0251\u0303",
    "r": "\u0280",
    "e": "\u025b",
    "g": "\u0292",
    "é": "e",
    "ç": "s",
}


def orthography_to_phonology(text: str) -> str:
    """Parse a written french into a phonologic representation"""
    text = text.lower()
    if text[-1:] in "tesb":
        text = text[:-1]
    for letter, sound in character_map.items():
        text = text.replace(letter, sound)
    return text
