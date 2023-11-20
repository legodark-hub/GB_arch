from Fabrics.item_fabric import ItemFabric
from Products.gold import Gold


class GoldGenerator(ItemFabric):
    def create_item(self):
        return Gold()