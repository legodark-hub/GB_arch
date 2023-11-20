from Fabrics.item_fabric import ItemFabric
from Products.silver import Silver


class SilverGenerator(ItemFabric):
    def create_item(self):
        return Silver()
