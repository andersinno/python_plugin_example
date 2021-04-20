import pluggy  # type: ignore

from python_plugin_example.hookspec import PluginExampleHookSpec
from python_plugin_example.plugins.chucknorris import ChuckNorrisPlugin
from python_plugin_example.plugins.icanhazdadjoke import ICanHazDadJokePlugin


class App:
    def __init__(self) -> None:
        self.pm: pluggy.PluginManager = pluggy.PluginManager("plugin_example")
        self.pm.add_hookspecs(PluginExampleHookSpec)

        self.pm.register(ChuckNorrisPlugin())
        self.pm.register(ICanHazDadJokePlugin())

    def display_jokes(self, amount: int) -> None:
        results = self.pm.hook.retrieve_joke(amount=amount)
        jokes = [joke for plugin in results for joke in plugin]
        for joke in jokes:
            print(joke)


if __name__ == "__main__":
    app = App()
    app.display_jokes(2)
