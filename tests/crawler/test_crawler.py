from tibia.crawler import Crawler
from unittest import mock


@mock.patch("downloader.Downloader")
def test_tibia_search_character(downlaoder_mock, snapshot, resume_html):
    tibia_url = "https://www.tibia.com/"
    character = "Rosha Runner"
    downloader = downlaoder_mock.return_value
    downloader.post.return_value = mock.Mock(text=resume_html)

    crawler = Crawler(tibia_url, downloader)
    parsed = crawler.get_tibia_information(character)
    snapshot.assert_match(parsed.__dict__)
