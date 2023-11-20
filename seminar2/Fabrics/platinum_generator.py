from Fabrics.item_fabric import ItemFabric
from Products.platinum import Platinum


class PlatinumGenerator(ItemFabric):
    def create_item(self):
        return Platinum()
