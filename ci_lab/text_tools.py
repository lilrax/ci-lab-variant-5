"""Text helper functions."""

def normalize_text(text: str) -> str:
    return " ".join(text.lower().split())

def word_count(text: str) -> int:
    normalized = normalize_text(text)
    if not normalized:
        return 0
    return len(normalized.split(" "))

def unique_words(text: str) -> set[str]:
    normalized = normalize_text(text)
    if not normalized:
        return set()
    return set(normalized.split(" "))
