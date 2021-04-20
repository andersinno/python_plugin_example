from typing import List

import requests

from python_plugin_example.hookimpl import hookimpl

CHUCK_NORRIS_API_ENDPOINT = "https://api.chucknorris.io/jokes/random"


class ChuckNorrisPlugin:
    @hookimpl
    def retrieve_joke(self, amount: int) -> List[str]:
        values = []
        for i in range(amount):
            response = requests.get(CHUCK_NORRIS_API_ENDPOINT)
            values.append(response.json().get("value", ""))

        jokes = [f"🤠 Chuck Norris: {value}" for value in values]
        return jokes
