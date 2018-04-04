from abc import ABCMeta, abstractmethod


class Port(object):
    __metaclass__ = ABCMeta
    """Abstract product. One of its subclasses will be created in factory methods"""

    @abstractmethod
    def __str__(self) -> str:
        pass


class HttpPort(Port):
    """Concrete product that represents http port"""

    def __str__(self) -> str:
        return '80'


class HttpSecurePort(Port):
    """Concrete product that represents https port"""

    def __str__(self) -> str:
        return '443'


class FTPPort(Port):
    """Concrete product that represents ftp port"""

    def __str__(self) -> str:
        return '21'
