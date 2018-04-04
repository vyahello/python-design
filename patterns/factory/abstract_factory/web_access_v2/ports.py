from abc import ABC, ABCMeta, abstractmethod


class Port(ABC):
    """An abstract product represents port to connect.
     One of its subclasses will be created in factory methods.
     """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self) -> str:
        pass


class HTTPPort(Port):
    """Concrete product that represents http port"""

    def __str__(self) -> str:
        return '80'


class HTTPSecurePort(Port):
    """Concrete product that represents https port"""

    def __str__(self) -> str:
        return '443'


class FTPPort(Port):
    """Concrete product that represents ftp port"""

    def __str__(self) -> str:
        return '21'


class FTPSecurePort(Port):
    """Concrete product that represents ftps port"""

    def __str__(self) -> str:
        return '990'
