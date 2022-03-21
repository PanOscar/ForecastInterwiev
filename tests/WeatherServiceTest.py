import unittest
from WeatherService import WeatherService
from LocationService import LocationService

class TestLocationService(unittest.TestCase):
    def test_getData_Sucess(self):
        from datetime import date

        today = date.today()

        # dd/mm/YY
        d = today.strftime("%d.%m.%Y")

        apikey = "eX6qpC7MHwWwumO5Jx5qQppkDFRfJMr8"
        city = "gdansk"
        location = LocationService(f"http://dataservice.accuweather.com/locations/v1/search?apikey={apikey}&q={city}")
        actual = WeatherService(f"http://dataservice.accuweather.com/currentconditions/v1/{location.getData()}?apikey={apikey}")
        expected = 'Date: '+d
        self.assertIn(expected, str(actual))

    def test_testFunction_Exception(self):
        with self.assertRaises(SystemExit) as exception_context:
            apikey = "eX6qpC7MHwWwumO5Jx5qQppkDFRfJMr8"
            city = "gdanskzsdd"
            location = LocationService(f"http://dataservice.accuweather.com/locations/v1/search?apikey={apikey}&q={city}")
            rm = WeatherService(f"http://dataservice.accuweather.com/currentconditions/v1/{location.getData()}?apikey={apikey}")
            rm.getData()

        self.assertEqual(
            exception_context.exception.code,
            1
        )