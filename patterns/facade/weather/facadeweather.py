from abc import ABC, ABCMeta, abstractmethod


class Weather(ABC):
    """Represent abstraction for specific weather."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def temperature(self) -> float:
        pass


class FacadeWeather(Weather):
    def __init__(self, data: iter) -> None:
        self._data = data

    def temperature(self) -> float:
        temp = 0
        for r in self._data:
            temp += r
        return temp/len(self._data)
