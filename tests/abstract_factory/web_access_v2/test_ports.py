from patterns.patterns.factory.abstract_factory.web_access_v2.ports import HTTPPort, HTTPSecurePort, FTPPort, \
    FTPSecurePort

_http = '80'
_https = '443'
_ftp = '21'
_ftps = '990'


def test_http_port():
    assert str(HTTPPort()) == _http


def test_https_port():
    assert str(HTTPSecurePort()) == _https


def test_ftp_port():
    assert str(FTPPort()) == _ftp


def test_ftps_port():
    assert str(FTPSecurePort()) == _ftps
