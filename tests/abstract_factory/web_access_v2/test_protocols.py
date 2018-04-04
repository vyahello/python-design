from patterns.patterns.factory.abstract_factory.web_access_v2.protocols import HTTPProtocol, HTTPSecureProtocol, \
    FTPProtocol, FTPSecureProtocol

_http = 'http'
_https = 'https'
_ftp = 'ftp'
_ftps = 'ftps'


def test_http_protocol():
    assert str(HTTPProtocol()) == _http


def test_https_protocol():
    assert str(HTTPSecureProtocol()) == _https


def test_ftp_protocol():
    assert str(FTPProtocol()) == _ftp


def test_ftps_protocol():
    assert str(FTPSecureProtocol()) == _ftps
