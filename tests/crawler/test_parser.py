from bs4 import BeautifulSoup
from freezegun import freeze_time

from tibia.parser import Parser


@freeze_time("2018-12-02 09:00:20")
def test_parse(snapshot, resume_html):
    data = Parser().parse(resume_html)
    snapshot.assert_match(data)

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
