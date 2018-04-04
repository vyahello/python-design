from abc import ABCMeta, abstractmethod
from bs4 import BeautifulStoneSoup
from patterns.factory.factory_method.web_access.ports import Port, HttpPort, HttpSecurePort, FTPPort
from urllib.request import urlopen


class Connector(object):
    """Abstract class to connect to remote resource"""
    __metaclass__ = ABCMeta  # Declares class as abstract class

    def __init__(self, is_secure: bool):
        self.is_secure = is_secure
        self._port = self.port_factory_method()
        self._protocol = self.protocol_factory_method()

    @abstractmethod
    def parse(self, content: str) -> str:
        """Parse web content
        This method should be redefined in a runtime"""
        pass

    def read(self, host: str, path: str):
        url = self._protocol + '://' + host + ':' + str(self._port) + path
        print('Connecting to', url)
        return urlopen(url, timeout=2).read()

    @abstractmethod
    def protocol_factory_method(self) -> str:
        """A factory method that must be redefined in subclass"""
        pass

    @abstractmethod
    def port_factory_method(self) -> Port:
        """Another factory method that must be redefined in subclass"""
        pass


class HTTPConnector(Connector):
    """A concrete creator that creates a HTTP connector and sets in runtime all its attributes"""

    def protocol_factory_method(self) -> str:
        if self.is_secure:
            return 'https'
        return 'http'

    def port_factory_method(self) -> Port:
        """Here HTTPPort and HTTPSecurePort are concrete objects created by factory method"""
        if self.is_secure:
            return HttpSecurePort()
        return HttpPort()

    def parse(self, content: str) -> str:
        """Parses web content"""
        filenames = []
        soup = BeautifulStoneSoup(content)
        links = soup.table.findAll('a')
        for link in links:
            filenames.append(link['href'])
        return '\n'.join(filenames)


class FTPConnector(Connector):
    """A concrete creator that creates a FTP connector and sets in runtime all its attributes"""

    def protocol_factory_method(self) -> str:
        return 'ftp'

    def port_factory_method(self) -> Port:
        return FTPPort()

    def parse(self, content: str) -> str:
        lines = content.split('\n')
        filenames = []
        for line in lines:
            splitted_line = line.split(None, 8)
            if len(splitted_line) == 9:
                filenames.append(splitted_line[-1])
        return '\n'.join(filenames)
