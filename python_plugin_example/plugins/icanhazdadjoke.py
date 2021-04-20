from typing import List

import requests

from python_plugin_example.hookimpl import hookimpl

DAD_JOKE_API_ENDPOINT = "https://icanhazdadjoke.com/"


class ICanHazDadJokePlugin:
    @hookimpl
    def retrieve_joke(self, amount: int) -> List[str]:
        headers = {
            "Accept": "application/json",
        }
        values = []
        for i in range(amount):
            response = requests.get(DAD_JOKE_API_ENDPOINT, headers=headers)
            values.append(response.json().get("joke", ""))

        jokes = [f"👨 Dad joke: {value}" for value in values]
        return jokes
