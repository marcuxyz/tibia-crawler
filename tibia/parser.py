import re
import unicodedata
from datetime import datetime

from bs4 import BeautifulSoup

ACCOUNT_STATUS_REGEX = r"(Account\sStatus\:)"


class Parser:
    def parse(self, html):
        parsed = BeautifulSoup(html, "html.parser")
        character_information = parsed.select_one("div.BoxContent table")

        return {
            "name":
            self.extract_name(character_information),
            "extract_former_name":
            self.extract_former_name(character_information),
            "sex":
            self.extract_sex(character_information),
            "vocation":
            self.extract_vocation(character_information),
            "level":
            self.extract_level(character_information),
            "achievement":
            self.extract_achievement(character_information),
            "word":
            self.extract_word(character_information),
            "residence":
            self.extract_residence(character_information),
            "last_login":
            self.extract_last_login(character_information),
            "account_status":
            self.extract_account_status(character_information),
            "deaths":
            self.extract_deaths(parsed),
            "all_characters":
            self.extract_all_characters(parsed),
            "updated_at":
            datetime.utcnow(),
        }

    def extract_account_status(self, html):
        result = html.find("td", string=re.compile(ACCOUNT_STATUS_REGEX))
        return self._get_information(result)

    def extract_last_login(self, html):
        result = html.find("td", string="Last Login:")
        if result:
            text = result.find_next("td").text
            return unicodedata.normalize('NFKD', text).encode('ascii','ignore')

    def extract_residence(self, html):
        result = html.find("td", string="Residence:")
        return self._get_information(result)

    def extract_word(self, html):
        result = html.find("td", string="World:")
        return self._get_information(result)

    def extract_achievement(self, html):
        result = html.find("td", string="Achievement Points:")
        return self._get_information(result)

    def extract_sex(self, html):
        result = html.find("td", string="Sex:")
        return self._get_information(result)

    def extract_level(self, html):
        result = html.find("td", string="Level:")
        return self._get_information(result)

    def extract_vocation(self, html):
        result = html.find("td", string="Vocation:")
        return self._get_information(result)

    def extract_name(self, html):
        result = html.find("td", string="Name:")
        return self._get_information(result)

    def extract_former_name(self, html):
        result = html.find("td", string="Former Names:")
        return self._get_information(result)

    def extract_deaths(self, html):
        pass

    def extract_all_characters(self, html):
        pass

    def character_not_found(self, html):
        pass

    def _get_information(self, result):
        if result:
            return result.find_next("td").text.strip()
