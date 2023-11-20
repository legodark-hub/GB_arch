from Fabrics.item_fabric import ItemFabric
from Products.diamond import Diamond


class DiamondGenerator(ItemFabric):
    def create_item(self):
        return Diamond()
