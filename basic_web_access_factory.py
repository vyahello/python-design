from http.client import HTTPConnection
from ftplib import FTP
from typing import Any


class SimpleFactory(object):
    """Represent simple factory."""

    @staticmethod # to run this method without class instance like SimpleFactory.build_connection()
    def build_connection(protocol: str) -> Any:
        host = '127.0.0.1'
        if protocol is 'http':
            return HTTPConnection(host)
        elif protocol is 'ftp':
            return FTP(host)
        raise RuntimeError('Unknown protocol')


if __name__ == '__main__':
    protocol = input('Please enter a protocol type: ')
    protocol = SimpleFactory.build_connection(protocol)
    protocol.connect()
    print(protocol.getresponse())
