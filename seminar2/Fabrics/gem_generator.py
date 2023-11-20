from Fabrics.item_fabric import ItemFabric
from Products.gem import Gem


class GemGenerator(ItemFabric):
    def create_item(self):
        return Gem()