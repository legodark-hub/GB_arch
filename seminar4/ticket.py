import datetime


class Ticket:
    def __init__(
        self,
        price: float,
        date: datetime,
        start_zone: int,
        finish_zone: int,
        is_luggage: bool,
        place: int,
        road_number: int,
    ):
        self.price = price
        self.date = date
        self.start_zone = start_zone
        self.finish_zone = finish_zone
        self.is_luggage = is_luggage
        self.place = place
        self.road_number = road_number

    def is_valid(self):
        current_date = datetime.now()
        return self.date >= current_date
