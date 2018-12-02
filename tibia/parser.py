import re
from util import normalize_text
from bs4 import BeautifulSoup
from model import Tibia

ACCOUNT_STATUS_REGEX = r"(Account\sStatus\:)"


class Parser:
    def parse(self, html):
        parsed = BeautifulSoup(html, "html.parser")

        return Tibia(
            name=self.extract_name(parsed),
            extract_former_name=self.extract_former_name(parsed),
            sex=self.extract_sex(parsed),
            vocation=self.extract_vocation(parsed),
            level=self.extract_level(parsed),
            achievement=self.extract_achievement(parsed),
            residence=self.extract_residence(parsed),
            world=self.extract_word(parsed),
            last_login=self.extract_last_login(parsed),
            account_status=self.extract_account_status(parsed),
            deaths=self.extract_deaths(parsed),
        )

    def extract_account_status(self, html):
        result = html.find("td", string=re.compile(ACCOUNT_STATUS_REGEX))
        return self._get_information(result)

    def extract_last_login(self, html):
        result = html.find("td", string="Last Login:")
        if result:
            return normalize_text(result.find_next("td").text)

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
        text = html.find("b", string="Character Deaths")
        if text:
            result = []
            rows = text.find_all_next("tr")

            for item in rows:
                if item.text == "Account Information":
                    break

                timestamp = normalize_text(
                    item.select_one("td:nth-of-type(1)").text.strip()
                )
                description = normalize_text(
                    item.select_one("td:nth-of-type(2)").text.strip()
                )

                result.append({"timestamp": timestamp, "description": description})

            return result

    def character_not_found(self, html):
        parsed = BeautifulSoup(html, "html.parser")
        result = parsed.find(string=re.compile(r"(does\snot\sexist.)"))
        return not bool(result)

    def _get_information(self, result):
        if result:
            return result.find_next("td").text.strip()
