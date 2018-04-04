from urllib.error import URLError

from patterns.factory.abstract_factory.web_access_v2.connector import DefConnector
from patterns.factory.abstract_factory.web_access_v2.factories import ConnectionFactory
from patterns.factory.abstract_factory.web_access_v2.parsers import HTTPParser, FTPParser
from patterns.factory.abstract_factory.web_access_v2.ports import HTTPPort, HTTPSecurePort, FTPPort, FTPSecurePort
from patterns.factory.abstract_factory.web_access_v2.protocols import HTTPProtocol, HTTPSecureProtocol, FTPProtocol, \
    FTPSecureProtocol

if __name__ == '__main__':
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'

    protocol = input('Connecting to {}. Which Protocol to use? (0-http, 1-ftp): '.format(domain))
    if int(protocol) == 0:
        is_secure = bool(input('Use secure connection? (1-yes, 0-no): '))
        factory = ConnectionFactory(is_secure,
                                    HTTPProtocol(), HTTPSecureProtocol(),
                                    HTTPPort(), HTTPSecurePort(),
                                    HTTPParser()
                                    )
    elif int(protocol) == 1:
        is_secure = bool(input('Use secure connection? (1-yes, 0-no): '))
        factory = ConnectionFactory(is_secure,
                                    FTPProtocol(), FTPSecureProtocol(),
                                    FTPPort(), FTPSecurePort(),
                                    FTPParser()
                                    )
    else:
        print('Sorry, wrong answer')

    connector = DefConnector(factory)
    try:
        content = connector.read(domain, path)
    except URLError:
        raise Exception('Cannot access resource with this method')
    else:
        print(connector.parse(content))

