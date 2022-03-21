import sys

from LocationService import LocationService
from WeatherService import WeatherService

if __name__ == '__main__':
    try:
        city = sys.argv[1]
    except IndexError:
        print("You did not specify a city in arguments")
        sys.exit(1)
    apikey = "eX6qpC7MHwWwumO5Jx5qQppkDFRfJMr8"

    location = LocationService(f"http://dataservice.accuweather.com/locations/v1/search?apikey={apikey}&q={city}")
    location.run()
    getTemp = WeatherService(f"http://dataservice.accuweather.com/currentconditions/v1/{location.getData()}?apikey={apikey}")

    getTemp.run()
    print(getTemp)
