# Переписать код в соответствии с Dependency Inversion Principle:


class Car:
    def init(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


class PetrolEngine:
    def start(self):
        pass
