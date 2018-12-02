from tibia.crawler import Crawler
from downloader import Downloader


class Character(Crawler):
    def __init__(self, character):
        super().__init__("https://www.tibia.com/", character, Downloader())
