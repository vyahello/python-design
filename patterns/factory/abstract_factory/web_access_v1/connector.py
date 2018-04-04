from abc import abstractmethod
from urllib.request import urlopen
from patterns.factory.abstract_factory.web_access_v1.factories import AbstractFactory


class Connector:
    """A client"""
    def __init__(self, factory: AbstractFactory):
        """factory is a AbstractFactory instance which creates all attributes of a connector according to factory
        class """
        self._protocol = factory.create_protocol()
        self._port = factory.create_port()
        self._parse = factory.create_parser()

    def read(self, host: str, path: str) -> None:
        url = str(self._protocol) + '://' + host + ':' + str(self._port) + path
        print('Connecting to', url)
        urlopen(url, timeout=2).read()

    @abstractmethod
    def parse(self):
        pass
