import requests
import sys


class RequestModel:
    def __init__(self, url):
        self.request = requests.get(url)

    def test(self):
        try:
            if self.request.status_code != 200:
                raise KeyError('ApiLimitReached')
        except KeyError as e:
            print("Url is not accessible or you have reached limit of requests for this api key. Error message: " + str(e))
            sys.exit(1)
    def getData(self):
        pass

    def run(self):
        self.test()
        self.getData()
