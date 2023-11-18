from ast import List
from seminar1.in_memory_model import IModelChangeObserver, IModelChanger
from seminar1.model_elements.camera import Camera
from seminar1.model_elements.flash import Flash
from seminar1.model_elements.poligonal_model import PoligonalModel
from seminar1.model_elements.scene import Scene


class ModelStore(IModelChanger):
    def __init__(self, changeObservers: [IModelChangeObserver]):
        self.models = [PoligonalModel]
        self.scenes = [Scene]
        self.flashes = [Flash]
        self.cameras = [Camera]
        self.changeObserver = changeObservers

    def get_scene(self, id):
        for scene in self.scenes:
            if scene.id == id:
                return scene
        return None

    def notify_change(self, sender) -> None:
        return super().notify_change(sender)
