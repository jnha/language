def orthography_to_phonology(text: str) -> str:
    """Convert from written spanish to a phonemic ipa transcription"""
    i = 0
    out = []
    text = text.lower()
    while i < len(text):
        if text[i] == "r":
            if text[i + 1] == "r":
                out.append("r")
            else:
                out.append("ɾ")
        elif text[i] == "l":
            if text[i + 1] == "l":
                out.append("ʎ")
            else:
                out.append("l")
        elif text[i] == "c":
            if text[i + 1] in "ei":
                out.append("θ")
            elif text[i + 1] == "h":
                out.append("t͡ʃ")
            else:
                out.append("k")
        elif text[i] == "h":
            pass
        elif text[i] == "q":
            out.append("q")
        elif text[i] == "y":
            if text[i - 1] not in "eaoiu" or text[i + 1] in "eaiou":
                out.append("ʝ")
        elif text[i] == ".":
            out.append(" ‖")
        elif text[i] == ",":
            out.append(" |")
        elif not text[i].isalpha():
            out.append(text[i])
        else:  # Default no change to handle numbers and foreign scripts
            out.append(text[i])
        i += 1
    return "".join(out)
