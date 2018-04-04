from patterns.factory.abstract_factory.web_access_v1.protocols import HttpProtocol, HttpSecureProtocol, \
    FTPProtocol

_http = 'http'
_https = 'https'
_ftp = 'ftp'


def test_http_protocol():
    assert str(HttpProtocol()) == _http


def test_https_protocol():
    assert str(HttpSecureProtocol()) == _https


def test_ftp_protocol():
    assert str(FTPProtocol()) == _ftp
