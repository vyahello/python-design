from abc import ABC, ABCMeta, abstractmethod


class Converter(ABC):
    """Represent abstraction for specific converter."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def value(self) -> float:
        pass


class KelToCel(Converter):
    """Represent kelvin to celsius converter."""

    def __init__(self, kelvin: float) -> None:
        self._kel = kelvin

    def value(self) -> float:
        return self._kel - 273.15
