from Products.i_game_item import IGameItem


class Diamond(IGameItem):
    def open(self):
        print("Diamond!")
