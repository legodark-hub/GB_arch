import datetime
from random import randint
from bus_route import BusRoute
from person import Person
from ticket import Ticket


class TicketStore:
    def __init__(self):
        self.routes = [BusRoute]

    def sell_ticket(
        self,
        person: Person,
        start_zone: int,
        finish_zone: int,
        date: datetime,
        is_luggage: bool,
    ):
        selected_route = self.find_matching_route(start_zone, finish_zone)
        if selected_route is None:
            print("Нет подходящего маршрута")
            return None

        ticket_price = self.calculate_ticket_price(start_zone, finish_zone, is_luggage)

        seat_number = self.assign_seat_number(selected_route)

        new_ticket = Ticket(
            price=ticket_price,
            date=date,
            start_zone=start_zone,
            finish_zone=finish_zone,
            is_luggage=is_luggage,
            place=seat_number,
            road_number=selected_route.id,
        )

        if self.process_payment(person, ticket_price):
            print(
                f"Билет продан"
            )
            return new_ticket
        else:
            print("Ошибка оплаты.")
            return None

    def find_matching_route(self, start_zone: int, finish_zone: int) -> BusRoute:
        pass

    def calculate_ticket_price(
        self, start_zone: int, finish_zone: int, is_luggage: bool
    ) -> float:
        pass

    def assign_seat_number(self, route: BusRoute) -> int:
        pass
    
    def process_payment(self, person: Person, amount: float) -> bool:
        pass