from random import choices, randint
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

# Веса для каждой награды
weights = [3, 1, 10, 10, 10, 10, 10]

for i in range(20):
    chosen_reward = choices(rewards, weights)[0]
    chosen_reward.create_item().open()
