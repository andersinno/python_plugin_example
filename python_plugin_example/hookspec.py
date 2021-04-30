from typing import Any, Callable, List, TypeVar, cast

import pluggy  # type: ignore

F = TypeVar("F", bound=Callable[..., Any])
hookspec = cast(Callable[[F], F], pluggy.HookspecMarker("python_plugin_example"))


class PluginExampleHookSpec:
    """
    Python Plugin Example Hook Specification
    """

    @hookspec
    def retrieve_joke(self, amount: int) -> List[str]:
        """
        Fired when retrieving jokes

        Args:
            amount: How many jokes should be returned

        Returns:
            A string containing a joke

        """
