class TransportZone:
    def __init__(self, zone_id: int, remark: str):
        self.id = zone_id
        self.remark = remark

    def update_remark(self, new_remark: str):
        self.remark = new_remark
