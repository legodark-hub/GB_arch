from Products.i_game_item import IGameItem


class Bronze(IGameItem):
    def open(self):
        print("Bronze!")
