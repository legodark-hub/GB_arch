class BusStop:
    def __init__(self, stop_id: int, name: str, attitude: float, latitude: float):
        self.id = stop_id
        self.name = name
        self.attitude = attitude
        self.latitude = latitude
        
    def get_coordinates(self):
        return [self.attitude, self.latitude]
