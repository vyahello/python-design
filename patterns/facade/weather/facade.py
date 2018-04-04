from patterns.facade.weather.cache import Cache
from patterns.facade.weather.converter import KelToCel
from patterns.facade.weather.data import WeatherProvider
from patterns.facade.weather.parser import Parser
from patterns.facade.weather.facadeweather import FacadeWeather


class Facade(object):
    def get_forecast(self, city: str, country: str) -> float:
        cache = Cache('myfile')
        cache_result = cache.load()
        if not cache_result:
            weather_provider = WeatherProvider()
            weather_data = weather_provider.get_weather_data(city, country)
            parser = Parser()
            parsed_data = parser.parse_weather_data(weather_data)
            weather = FacadeWeather(parsed_data)
            converter = KelToCel(weather.temperature())
            temp_celsius = converter.value()
            cache.save(temp_celsius)
            return temp_celsius
        return cache_result
