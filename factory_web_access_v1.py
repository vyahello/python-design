from urllib.error import URLError
from patterns.factory.abstract_factory.web_access_v1.connector import Connector
from patterns.factory.abstract_factory.web_access_v1.factories import HttpFactory, FTPFactory

if __name__ == '__main__':
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'

    protocol = input('Connecting to {}. Which Protocol to use? (0-http, 1-ftp): '.format(domain))
    if int(protocol) == 0:
        is_secure = bool(input('Use secure connection? (1-yes, 0-no): '))
        factory = HttpFactory(is_secure)
    elif int(protocol) == 1:
        is_secure = False
        factory = FTPFactory(is_secure)
    else:
        print('Sorry, wrong answer')

    connector = Connector(factory)
    try:
        content = connector.read(domain, path)
    except URLError:
        raise Exception('Cannot access resource with this method')
    else:
        print(connector.parse(content))
