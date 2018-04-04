from abc import ABCMeta, ABC, abstractmethod
from urllib.request import urlopen
from patterns.factory.abstract_factory.web_access_v2.factories import Factory


class Connector(ABC):
    """Abstract connector."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self, host: str, path: str) -> None:
        pass

    @abstractmethod
    def parse(self, content: str) -> str:
        pass


class DefConnector(Connector):
    """A client connector."""
    def __init__(self, factory: Factory):
        """factory is a Factory instance which creates all attributes of a connector according to factory class. """
        self._factory = factory

    def read(self, host: str, path: str) -> None:
        url = str(self._factory.create_protocol()) + '://' + host + ':' + str(self._factory.create_port()) + path
        print('Connecting to', url)
        urlopen(url, timeout=2).read()

    def parse(self, content: str) -> str:
        parser = self._factory.create_parser()
        return parser(content)
