from bs4 import BeautifulSoup
from freezegun import freeze_time
from tibia.parser import Parser


@freeze_time("2018-12-02 09:00:20")
def test_parse(resume_html):
    data = Parser().parse(resume_html)
    assert data


def test_extract_name(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    character = parsed.select_one("div.BoxContent table")
    text = Parser().extract_name(character)
    snapshot.assert_match(text)

def test_extract_former_name(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    character = parsed.select_one("div.BoxContent table")
    text = Parser().extract_former_name(character)
    snapshot.assert_match(text)

def test_extract_sex(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    character = parsed.select_one("div.BoxContent table")
    text = Parser().extract_sex(character)
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
    character = parsed.select_one("div.BoxContent table")
    text = Parser().extract_residence(character)
    snapshot.assert_match(text)


def test_extract_world(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    character = parsed.select_one("div.BoxContent table")
    text = Parser().extract_word(character)
    snapshot.assert_match(text)


def test_extract_level(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    character = parsed.select_one("div.BoxContent table")
    text = Parser().extract_level(character)
    snapshot.assert_match(text)


def test_extract_vocation(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    character = parsed.select_one("div.BoxContent table")
    text = Parser().extract_vocation(character)
    snapshot.assert_match(text)


def test_extract_achievement(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    character = parsed.select_one("div.BoxContent table")
    text = Parser().extract_achievement(character)
    snapshot.assert_match(text)


def test_extract_achievement(snapshot, resume_html):
    parsed = BeautifulSoup(resume_html, "html.parser")
    character = parsed.select_one("div.BoxContent table")
    text = Parser().extract_achievement(character)
    snapshot.assert_match(text)