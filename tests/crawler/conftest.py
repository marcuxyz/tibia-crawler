import pytest
from util import load_mockup


@pytest.fixture(scope="module")
def resume_html():
    return load_mockup("resume.html")
