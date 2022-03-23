import logging
import sys
from request_model import RequestModel


class LocationService(RequestModel):
    def get_data(self):
        try:
            result = self.request.json()
            rt = result[0]["Key"]
            return rt
        except Exception:
            logging.exception("Request does not contain any data")

