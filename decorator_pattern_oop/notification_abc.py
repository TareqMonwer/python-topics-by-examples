import abc


class Notifier(abc.ABC):
    @abc.abstractmethod
    def send(self, message: str):
        pass
