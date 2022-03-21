import unittest
from LocationService import LocationService


class TestLocationService(unittest.TestCase):
    def test_getData_Sucess(self):
        apikey = "eX6qpC7MHwWwumO5Jx5qQppkDFRfJMr8"
        city = "gdansk"
        actual = LocationService(f"http://dataservice.accuweather.com/locations/v1/search?apikey={apikey}&q={city}").getData()
        expected = '1-275174_1_AL'
        self.assertEqual(actual, expected)

    def test_testFunction_Exception(self):
        with self.assertRaises(SystemExit) as exception_context:
            apikey = "eX6qpC7MHwWwumO5Jx5qQppkDFRfJMr8"
            city = "gdanskzsdd"
            rm = LocationService(f"http://dataservice.accuweather.com/locations/v1/search?apikey={apikey}&q={city}")
            rm.getData()

        self.assertEqual(
            exception_context.exception.code,
            1
        )