from ast import List
from seminar1.model_elements.poligon import Poligon

from seminar1.model_elements.texture import Texture


class PoligonalModel:
    def __init__(self, texture: List[Texture]):
        self.poligons = [Poligon]
        self.textures = texture