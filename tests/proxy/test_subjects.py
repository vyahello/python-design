from patterns.patterns.proxy.subjects import RealSubject, ProxySubject


def test_real_subject():
    assert RealSubject().sort().__class__ == list


def test_proxy_subject():
    assert ProxySubject().sort().__class__ == list
