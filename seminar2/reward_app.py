
from abc import ABC, abstractmethod
from random import randint


class IGameItem(ABC):
    @abstractmethod
    def open(self):
        pass


class ItemFabric(ABC):
    @abstractmethod
    def create_item(self):
        pass


class Gold(IGameItem):
    def open(self):
        print('Gold!')


class Gem(IGameItem):
    def open(self):
        print('Gem!')


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()


if __name__ == '__main__':
    rewards = [GoldGenerator(), GemGenerator()]

    for i in range(20):
        rewards[randint(0, 1)].create_item().open()