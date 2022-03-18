import requests as r

class LocationService:
    def __init__(self,city):
        self.city = city

    def getCity(self):
        result = r.get(f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey=aL5cjAhZAkvSRI7QfmkyaXrmDYlGJHie&q={self.city}")