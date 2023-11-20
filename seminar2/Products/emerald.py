from Products.i_game_item import IGameItem


class Emerald(IGameItem):
    def open(self):
        print("Emerald!")
