from abc import ABC, abstractmethod


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass