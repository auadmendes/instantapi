def break_text(text: str, piece_length: int = 1000, overlay: int = 200) -> list[str]:
    """
    Splits a long string into overlapping chunks.
    """
    if piece_length <= overlay:
        raise ValueError("Piece length must be greater than overlay.")

    pieces = []
    start = 0
    while start < len(text):
        end = start + piece_length
        piece = text[start:end]
        pieces.append(piece)
        start += piece_length - overlay

    return pieces
