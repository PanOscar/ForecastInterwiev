import unittest

from request_model import RequestModel


class TestRequestModel(unittest.TestCase):
    def test_testFunction_Exception(self):
        """Testing request codes Exception"""
        with self.assertLogs() as response:
            rm = RequestModel("http://dataservice.accuweather.com/locations/v1/search?apikey=xxx&q=gdansk")
            rm.test()

        self.assertEqual(len(response), 2)
        self.assertTrue(response.records[0].getMessage().startswith("40"))
