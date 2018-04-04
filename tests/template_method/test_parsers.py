import pytest
from patterns.template_method.parsers import AbstractNewsParser, YahooParser, GoogleParser

_yahoo_url = 'http://news.yahoo.com/rss/'
_google_url = 'https://news.google.com/news/feeds?output=atom'


def test_abstract_news_parser():
    with pytest.raises(TypeError):
        AbstractNewsParser()


def test_yahoo_parser_url():
    assert YahooParser().get_url() == _yahoo_url


def test_google_parser_url():
    assert GoogleParser().get_url() == _google_url
