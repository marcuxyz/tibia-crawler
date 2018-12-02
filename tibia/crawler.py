from urllib.parse import urljoin
from tibia.parser import Parser
import json


class Crawler:
    def __init__(self, tibia_url, character, downloader):
        self.tibia_url = tibia_url
        self.downlaoder = downloader
        self.parser = Parser()
        self.get_tibia_information(character)

    def get_tibia_information(self, character):
        character_url = urljoin(self.tibia_url, "community/?subtopic=characters")
        params = self.config_params(character)
        response = self.downlaoder.post(character_url, data=params)

        if self.parser.character_not_found(response.text):
            parsed = self.parser.parse(response.text)
            self.save_data(parsed.__dict__)
            return parsed

    def config_params(self, character):
        return {"name": character, "Submit.x": 0, "Submit.y": 0}

    def save_data(self, data):
        name = data.get("name")
        with open(f"tibia/database/{name}.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
            print("Personagem salvo com sucesso!")
