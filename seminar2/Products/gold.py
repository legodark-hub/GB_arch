from Products.i_game_item import IGameItem


class Gold(IGameItem):
    def open(self):
        print("Gold!")