from patterns.factory.factory_method.web_access.connectors import HTTPConnector, FTPConnector
from urllib.error import URLError

if __name__ == '__main__':
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'

    protocol = input('Connecting to {}. Which Protocol to use? (0-http, 1-ftp): '.format(domain))
    if protocol == 0:
        is_secure = bool(input('Use secure connection? (1-yes, 0-no): '))
        connector = HTTPConnector(is_secure)
    else:
        is_secure = False
        connector = FTPConnector(is_secure)
    try:
        content = connector.read(domain, path)
    except URLError:
        raise Exception('Cannot access resource with this method')
    else:
        print(connector.parse(content))
