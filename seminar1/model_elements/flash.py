class Flash:
    def __init__(self):
        self.location = Point3D
        self.angle = Angle3D
        self.color = Color
        self.power = float
    
    def rotate(self, Angle3D):
        self.angle = Angle3D
    
    def move(self, Point3D):
        self.location = Point3D