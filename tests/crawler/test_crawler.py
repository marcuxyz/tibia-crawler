from tibia.crawler import Crawler
from unittest import mock
import pytest
from util import load_mockup


@pytest.fixture
def resume_html():
    return load_mockup("resume.html")


@mock.patch("downloader.Downloader")
def test_tibia_search_character(downlaoder_mock, snapshot, resume_html):
    tibia_url = "https://www.tibia.com/"
    character = "Rosha Runner"
    downloader = downlaoder_mock.return_value
    downloader.post.return_value = mock.Mock(text=resume_html)

    crawler = Crawler(tibia_url, character, downloader)
    snapshot.assert_match(crawler.get_tibia_information(character).__dict__)
