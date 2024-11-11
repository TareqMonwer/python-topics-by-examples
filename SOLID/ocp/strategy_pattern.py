"""The Strategy Pattern is a common way to adhere to OCP. This pattern allows to define a family of algorithms (or strategies), encapsulate each one, and make them interchangeable."""

import abc
from typing import Any


# Strategy interface
class Strategy(abc.ABC):
    @abc.abstractmethod
    def execute(self, data: Any):
        pass


class Context:
    """Strategy director class"""

    def __init__(self, strategy: Strategy) -> None:
        self.strategy: Strategy = strategy

    def execute_strategy(self, data: Any):
        self.strategy.execute(data)


# Concrete strategies
class PodcastListenerStrategy(Strategy):
    def execute(self, data: dict[str, list[str]]):
        print("Listener has this tools: ", data.items())


class MusicListenerStrategy(Strategy):
    def execute(self, data: list[str]):
        print("Playlist has these songs: ", data)


podcast_tools: dict[str, list[str]] = {"play_by_topics": ["art", "coding"]}
music_playlist: list[str] = ["music a", "music b", "music c", "music d", "music e"]

context = Context(PodcastListenerStrategy())
context.execute_strategy(podcast_tools)

context = Context(MusicListenerStrategy())
context.execute_strategy(music_playlist)
