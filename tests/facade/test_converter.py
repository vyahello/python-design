from patterns.facade.weather.converter import KelToCel

_kelvin = 300


def test_kel_to_cel():
    assert KelToCel(_kelvin).value() == 26.850000000000023
