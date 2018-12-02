from urllib.parse import urljoin
from tibia.parser import Parser


class Crawler:
    def __init__(self, tibia_url, downloader):
        self.tibia_url = tibia_url
        self.downlaoder = downloader
        self.parser = Parser()

    def get_tibia_information(self, character):
        character_url = urljoin(self.tibia_url, "community/?subtopic=characters")
        params = self.config_params(character)
        resppassonse = self.downlaoder.post(character_url, data=params)
        return self.parser.parse(response.text)

    def config_params(self, character):
        return {"name": character, "Submit.x": 0, "Submit.y": 0}
