from abc import ABC, ABCMeta, abstractmethod


class Protocol(ABC):
    """An abstract product represents port to connect.
     One of its subclasses will be created in factory methods.
     """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self) -> str:
        pass


class HttpProtocol(Protocol):
    """Concrete product that represents http port"""

    def __str__(self) -> str:
        return 'http'


class HttpSecureProtocol(Protocol):
    """Concrete product that represents https port"""

    def __str__(self) -> str:
        return 'https'


class FTPProtocol(Protocol):
    """Concrete product that represents ftp port"""

    def __str__(self) -> str:
        return 'ftp'
