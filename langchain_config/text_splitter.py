def split_text(text, chunk_size=500):
    """
    Divide textos longos em pedaços menores.
    """
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
