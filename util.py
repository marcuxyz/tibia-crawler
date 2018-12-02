import unicodedata


def load_mockup(mockup_name, encoding="utf-8"):
    with open(f"tests/mockup/{mockup_name}", encoding=encoding, mode="r") as f:
        return f.read()


def normalize_text(date: str) -> str:
    return unicodedata.normalize("NFKD", date).encode("ascii", "ignore").decode("utf-8")
