from bus_stop import BusStop


class BusRoute:
    def __init__(self, route_id: int, remark: str, capacity: int, bus_stops: [BusStop]):
        self.id = route_id
        self.remark = remark
        self.capacity = capacity
        self.bus_stops = bus_stops
        
    def add_bus_stop(self, bus_stop: BusStop):
        self.bus_stops.append(bus_stop)

    def remove_bus_stop(self, bus_stop: BusStop):
        if bus_stop in self.bus_stops:
            self.bus_stops.remove(bus_stop)

    def get_bus_stops_count(self):
        return len(self.bus_stops)

    def display_route_info(self):
        print(f"Route ID: {self.id}")
        print(f"Remark: {self.remark}")
        print(f"Capacity: {self.capacity}")
        print("Bus Stops:")
        for stop in self.bus_stops:
            print(f" - {stop.name}")
