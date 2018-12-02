import pytest
from bs4 import BeautifulSoup

from tibia.parser import Parser
from util import load_mockup


@pytest.fixture
def resume_html():
    return load_mockup("resume.html")


@pytest.fixture
def not_found_html():
    return load_mockup("not_found.html")


def test_extract_name(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    text = Parser().extract_name(parsed)
    snapshot.assert_match(text)


def test_extract_former_name(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    text = Parser().extract_former_name(parsed)
    snapshot.assert_match(text)


def test_extract_sex(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    text = Parser().extract_sex(parsed)
    snapshot.assert_match(text)


def test_extract_account_status(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    text = Parser().extract_account_status(parsed)
    snapshot.assert_match(text)


def test_extract_last_login(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    text = Parser().extract_last_login(parsed)
    snapshot.assert_match(text)


def test_extract_residence(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    text = Parser().extract_residence(parsed)
    snapshot.assert_match(text)


def test_extract_world(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    text = Parser().extract_word(parsed)
    snapshot.assert_match(text)


def test_extract_level(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    text = Parser().extract_level(parsed)
    snapshot.assert_match(text)


def test_extract_vocation(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    text = Parser().extract_vocation(parsed)
    snapshot.assert_match(text)


def test_extract_achievement(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    text = Parser().extract_achievement(parsed)
    snapshot.assert_match(text)


def test_extract_achievement(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    text = Parser().extract_achievement(parsed)
    snapshot.assert_match(text)


def test_extract_deaths(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    deaths = Parser().extract_deaths(parsed)
    for death in deaths:
        snapshot.assert_match(death)


def test_not_found(snapshot, not_found_html):
    confirmation = Parser().character_not_found(not_found_html)
    assert not confirmation == True
