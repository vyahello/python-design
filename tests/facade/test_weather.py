from patterns.facade.weather.facadeweather import FacadeWeather

_temp = [23.01, 25.03, 20.60]


def test_facade_weather():
    assert FacadeWeather(_temp).temperature() == 22.880000000000006
