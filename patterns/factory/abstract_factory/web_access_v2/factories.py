from abc import ABC, ABCMeta, abstractmethod
from patterns.factory.abstract_factory.web_access_v2.parsers import Parser
from patterns.factory.abstract_factory.web_access_v2.ports import Port
from patterns.factory.abstract_factory.web_access_v2.protocols import Protocol


class Factory(ABC):
    """This class interface provides 3 methods to implement in its subclasses:
    create_protocol, create_port and create_parser."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_protocol(self) -> Protocol:
        pass

    @abstractmethod
    def create_port(self) -> Port:
        pass

    @abstractmethod
    def create_parser(self) -> Parser:
        pass


class ConnectionFactory(Factory):
    """Concrete factory for building connection"""

    def __init__(self, is_secure: bool, protocol: Protocol, secure_protocol: Protocol, port: Port, secure_port: Port,
                 parser: Parser):
        self._is_secure = is_secure
        self._protocol = protocol
        self._secure_protocol = secure_protocol
        self._port = port
        self._secure_port = secure_port
        self._parser = parser

    def create_protocol(self) -> Protocol:
        if self._is_secure:
            return self._secure_protocol
        return self._protocol

    def create_port(self) -> Port:
        if self._is_secure:
            return self._secure_port
        return self._port

    def create_parser(self) -> Parser:
        return self._parser
