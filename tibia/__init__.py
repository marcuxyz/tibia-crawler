from tibia.crawler import Crawler
from downloader import Downloader


class TibiaCharacter(Crawler):
    def __init__(self):
        tibia_url = "https://www.tibia.com/"
        super().__init__(self, tibia_url, Downloader())
