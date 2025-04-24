from modelos.estacion import StationNode
from modelos.encriptacion import Encryptor

class WeatherController:
    def __init__(self):
        self.head_station = None
        self.encryptor = Encryptor()

    def add_station(self, name):
        new_station = StationNode(name)
        if not self.head_station:
            self.head_station = new_station
        else:
            current = self.head_station
            while current.next_station:
                current = current.next_station
            current.next_station = new_station

    def get_station_by_name(self, name):
        current = self.head_station
        while current:
            if current.name == name:
                return current
            current = current.next_station
        return None

    def add_weather_to_station(self, station_name, weather_info):
        station = self.get_station_by_name(station_name)
        if station:
            encrypted = self.encryptor.encrypt(weather_info)
            station.add_weather(encrypted)
