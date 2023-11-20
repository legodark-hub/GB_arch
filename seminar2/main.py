from random import randint
from Fabrics.gem_generator import GemGenerator
from Fabrics.gold_generator import GoldGenerator
from Fabrics.bronze_generator import BronzeGenerator
from Fabrics.diamond_generator import DiamondGenerator
from Fabrics.emerald_generator import EmeraldGenerator
from Fabrics.platinum_generator import PlatinumGenerator
from Fabrics.silver_generator import SilverGenerator


rewards = [
    GoldGenerator(),
    GemGenerator(),
    BronzeGenerator(),
    DiamondGenerator(),
    EmeraldGenerator(),
    PlatinumGenerator(),
    SilverGenerator(),
]

for i in range(20):
    rewards[randint(0, 6)].create_item().open()
