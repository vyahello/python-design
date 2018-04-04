from urllib.request import urlopen
from urllib.parse import quote


class WeatherProvider(object):
    def __init__(self):
        self._api_url = 'http://api.openweathermap.org/data/2.5/forecast?q={},{}'

    def get_weather_data(self, city: str, country: str):
        city = quote(city)
        url = self._api_url.format(city, country)
        return urlopen(url).read()
