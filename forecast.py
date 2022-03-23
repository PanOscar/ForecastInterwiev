import config
import logging
import sys

from location_service import LocationService
from weather_service import WeatherService


if __name__ == '__main__':
    try:
        city = sys.argv[1]
    except IndexError:
        logging.exception("You did not specify a city in arguments")
    apikey = config.API_KEY_SERVICE

    location = LocationService(f"http://dataservice.accuweather.com/locations/v1/search?apikey={apikey}&q={city}")
    location.run()
    get_temp = WeatherService(f"http://dataservice.accuweather.com/currentconditions/v1/{location.get_data()}?apikey={apikey}")

    get_temp.run()
    print(get_temp)
