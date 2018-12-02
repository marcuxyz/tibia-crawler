import pytest


def load_mockup(mockup_name, encoding="utf-8"):
    with open(f"tests/mockup/{mockup_name}", encoding=encoding, mode="r") as f:
        return f.read()


@pytest.fixture(scope="module")
def resume_html():
    return load_mockup("resume.html")