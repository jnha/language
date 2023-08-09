"""French Language"""

character_map = {
    "ch": "\u0283",
    "tt": "t",
    "r": "\u0280",
    "e": "\u025b",
}


def orthography_to_phonology(text: str) -> str:
    """Parse a written french into a phonologic representation"""
    if text[-1:] in ("t", "e"):
        text = text[:-1]
    for letter, sound in character_map.items():
        text = text.replace(letter, sound)
    return text
