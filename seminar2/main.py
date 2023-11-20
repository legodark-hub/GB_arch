from random import randint
from Fabrics.gem_generator import GemGenerator
from Fabrics.gold_generator import GoldGenerator


rewards = [GoldGenerator(), GemGenerator()]

for i in range(20):
    rewards[randint(0, 1)].create_item().open()
