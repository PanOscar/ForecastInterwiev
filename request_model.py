import logging
import sys

import requests
from abc import abstractmethod


class RequestModel:
    def __init__(self, url):
        self.request = requests.get(url)

    def test(self):
        """Test if apikey is still available"""
        try:
            if self.request.status_code != 200:
                self.request.raise_for_status()
            else:
                self.request.status_code = self.request.ok
        except Exception as e:
            logging.exception(str(e))

    @abstractmethod
    def get_data(self):
        """Abstract method to implement.
        Get data from Api about exact service
        """
        raise NotImplemented("Subclasses should implement this!")

    def run(self):
        """Run a test and data at once. Returns nothing"""
        self.test()
        self.get_data()
