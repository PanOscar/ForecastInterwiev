import sys
from RequestModel import RequestModel


class LocationService(RequestModel):
    def __init__(self, url):
        super().__init__(url)

    def getData(self):
        try:
            result = self.request.json()
            rt = result[0]["Key"]
            return rt
        except (KeyError, IndexError) as e:
            print("Data not found")
            sys.exit(1)

