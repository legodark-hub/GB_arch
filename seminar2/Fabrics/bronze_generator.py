from Fabrics.item_fabric import ItemFabric
from Products.bronze import Bronze


class BronzeGenerator(ItemFabric):
    def create_item(self):
        return Bronze()
