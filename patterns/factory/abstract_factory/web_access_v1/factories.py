from abc import ABC, ABCMeta, abstractmethod
from patterns.factory.abstract_factory.web_access_v1.ports import HttpSecurePort, HttpPort, Port, FTPPort
from patterns.factory.abstract_factory.web_access_v1.parsers import Parser, HttpParser, FTPParser
from patterns.factory.abstract_factory.web_access_v1.protocols import Protocol, HttpProtocol, HttpSecureProtocol, \
    FTPProtocol


class AbstractFactory(ABC):
    """This class interface provides 3 methods to implement in its subclasses:
    create_protocol, create_port and create_parser."""
    __metaclass__ = ABCMeta

    def __init__(self, is_secure: bool):
        self.is_secure = is_secure

    @abstractmethod
    def create_protocol(self) -> Protocol:
        pass

    @abstractmethod
    def create_port(self) -> Port:
        pass

    @abstractmethod
    def create_parser(self) -> Parser:
        pass


class HttpFactory(AbstractFactory):
    """Concrete factory for building HTTP connection"""

    def create_protocol(self) -> Protocol:
        if not self.is_secure:
            return HttpProtocol()
        return HttpSecureProtocol()

    def create_port(self) -> Port:
        if self.is_secure:
            return HttpSecurePort()
        return HttpPort()

    def create_parser(self) -> Parser:
        return HttpParser()


class FTPFactory(AbstractFactory):
    """Concrete factory for building FTP connection"""

    def create_protocol(self) -> Protocol:
        return FTPProtocol()

    def create_port(self) -> Port:
        return FTPPort()

    def create_parser(self) -> Parser:
        return FTPParser()
