import requests
from collections import namedtuple


class Downloader:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, cookies=None):
        response = self.session.get(url, params=params, verify=False, cookies=cookies)
        response.raise_for_status()

        return response

    def post(self, url, data=None, params=None, cookies=None, headers=None):
        response = self.session.post(
            url,
            data=data,
            params=params,
            verify=False,
            headers=headers,
            cookies=cookies,
        )
        response.raise_for_status()

        return response

    def close(self):
        self.session.close()
