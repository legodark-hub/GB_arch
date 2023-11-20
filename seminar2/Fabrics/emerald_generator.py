from Fabrics.item_fabric import ItemFabric
from Products.emerald import Emerald


class EmeraldGenerator(ItemFabric):
    def create_item(self):
        return Emerald()
