import config
import unittest
from unittest.mock import Mock

from location_service import LocationService


class TestLocationService(unittest.TestCase):
    def test_getData_Success(self):
        """" Testing if function Location Service return good data"""
        apikey = config.API_KEY_SERVICE
        city = "gdansk"
        actual = LocationService(
            f"http://dataservice.accuweather.com/locations/v1/search?apikey={apikey}&q={city}").get_data()
        expected = '1-275174_1_AL'
        self.assertEqual(actual, expected)

    def test_testFunction_Exception(self):
        """" Testing if function Location Service return exception"""
        with self.assertLogs() as exception_context:
            apikey = config.API_KEY_SERVICE
            city = "gdanskzsdd"
            rm = LocationService(f"http://dataservice.accuweather.com/locations/v1/search?apikey={apikey}&q={city}")
            rm.get_data()

        self.assertEqual(len(exception_context), 2)
        self.assertTrue(exception_context.records[0].getMessage().startswith("Reques"))
