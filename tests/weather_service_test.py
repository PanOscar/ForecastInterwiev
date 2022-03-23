import unittest
import config
from weather_service import WeatherService
from location_service import LocationService

class TestLocationService(unittest.TestCase):
    def test_getData_Success(self):
        """" Testing if function Weather Service return good data"""
        from datetime import date

        today = date.today()

        # dd/mm/YY
        d = today.strftime("%d.%m.%Y")

        apikey = config.API_KEY_SERVICE
        city = "gdansk"
        location = LocationService(f"http://dataservice.accuweather.com/locations/v1/search?apikey={apikey}&q={city}")
        actual = WeatherService(f"http://dataservice.accuweather.com/currentconditions/v1/{location.get_data()}?apikey={apikey}")
        expected = 'Date: '+d
        self.assertIn(expected, str(actual))

    def test_testFunction_Exception(self):
        with self.assertLogs() as exception_context:
            apikey = config.API_KEY_SERVICE
            city = "gdanskzsdd"
            location = LocationService(f"http://dataservice.accuweather.com/locations/v1/search?apikey={apikey}&q={city}")
            rm = WeatherService(f"http://dataservice.accuweather.com/currentconditions/v1/{location.get_data()}?apikey={apikey}")
            rm.get_data()

        self.assertEqual(len(exception_context), 2)
        self.assertTrue(exception_context.records[0].getMessage().startswith("Request"))