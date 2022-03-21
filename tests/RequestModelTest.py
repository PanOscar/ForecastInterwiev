import unittest
from RequestModel import RequestModel


class TestRequestModel(unittest.TestCase):
    def test_testFunction_Exception(self):
        with self.assertRaises(SystemExit) as exception_context:
            rm = RequestModel("http://dataservice.accuweather.com/locations/v1/search?apikey=xxx&q=gdansk")
            rm.test()

        self.assertEqual(
            exception_context.exception.code,
            1
        )