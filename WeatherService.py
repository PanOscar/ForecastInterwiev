import sys

from RequestModel import RequestModel
from WeatherModel import WeatherModel


class WeatherService(RequestModel):
    def __init__(self, url):
        super().__init__(url)

    def getData(self):
        try:
            result = self.request.json()
            model = WeatherModel(result[0]["LocalObservationDateTime"][:10],
                                 result[0]["Temperature"]["Metric"]["Value"])
            return model
        except KeyError:
            print("Data not found")
            sys.exit(1)

    def __repr__(self):
        return f"Date: {self.getData().date} Temperature {self.getData().temp}°C"
