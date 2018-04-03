from abc import ABC, ABCMeta, abstractmethod
import datetime


class Observer(ABC):
    """Abstract class for observers, provides notify method as interface for subjects"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def notify(self, unix_timestamp: float) -> str:
        pass


class USATimeObserver(Observer):
    def __init__(self, name: str):
        self._name = name

    def notify(self, unix_timestamp: float) -> str:
        time = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d %I:%M:%S%p')
        print('Observer', self._name, 'says:', time)
        return "Observer {} says: {}".format(self._name, time)


class EUTimeObserver(Observer):
    def __init__(self, name: str):
        self._name = name

    def notify(self, unix_timestamp: float) -> str:
        time = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d %I:%M:%S%p')
        print('Observer', self._name, 'says:', time)
        return "Observer {} says: {}".format(self._name, time)
