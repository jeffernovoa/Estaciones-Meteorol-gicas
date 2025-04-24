from clima_data import ClimaData  

class StationNode:
    def __init__(self, name):
        self.name = name
        self.weather_head = None
        self.next_station = None

    def add_weather(self, encrypted_data):
        new_node = ClimaData(encrypted_data)
        if not self.weather_head:
            self.weather_head = new_node
        else:
            current = self.weather_head
            while current.next:
                current = current.next
            current.next = new_node
