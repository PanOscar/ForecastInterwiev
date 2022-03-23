import logging
import sys

from request_model import RequestModel
from weather_model import WeatherModel


class WeatherService(RequestModel):
    def __init__(self, url):
        super().__init__(url)

    def get_data(self):
        try:
            result = self.request.json()
            model = WeatherModel(result[0]["LocalObservationDateTime"][:10],
                                 result[0]["Temperature"]["Metric"]["Value"])
            return model
        except Exception:
            logging.exception("Request does not contain any data")

    def __repr__(self):
        return f"Date: {self.get_data().date} Temperature {self.get_data().temp}°C"
