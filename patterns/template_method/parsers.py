from typing import List, Dict
from xml.dom.minidom import parseString
from urllib.request import urlopen


class AbstractNewsParser(object):
    def __init__(self) -> None:
        """Simulates behaviour of abstract class"""

        # Prohibit creating class instance
        if self.__class__ is AbstractNewsParser:
            raise TypeError('abstract class cannot be instantiated')

    def print_top_new(self) -> None:
        """A Template method. Returns 3 latest news for every news website."""

        url = self.get_url()
        raw_content = self.get_raw_content(url)
        content = self.parse_content(raw_content)
        cropped = self.crop(content)
        for item in cropped:
            print('Title: ', item['title'])
            print('Content: ', item['content'])
            print('Link: ', item['link'])
            print('Published: ', item['published'])
            print('Id: ', item['id'])

    def crop(self, parsed_content: List[Dict[str, str]], max_items: int = 3) -> List[Dict[str, str]]:
        return parsed_content[:max_items]

    def parse_content(self, content: str) -> List[Dict[str, str]]:
        """Has to be implemented in subclasses"""

        raise NotImplementedError()

    def get_raw_content(self, url: str) -> str:
        return urlopen(url).read()

    def get_url(self) -> str:
        """Has to be implemented in subclasses."""

        raise NotImplementedError()


class YahooParser(AbstractNewsParser):
    def get_url(self) -> str:
        return 'http://news.yahoo.com/rss/'

    def parse_content(self, content: str) -> List[Dict[str, str]]:
        parsed_content = []
        dom = parseString(content)
        for node in dom.getElementsByTagName('item'):
            parsed_item = {}
            try:
                parsed_item['title'] = node.getElementsByTagName('title')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['title'] = None
            try:
                parsed_item['content'] = node.getElementsByTagName('content')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['content'] = None
            try:
                parsed_item['link'] = node.getElementsByTagName('link')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['link'] = None
            try:
                parsed_item['id'] = node.getElementsByTagName('guid')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['id'] = None
            try:
                parsed_item['published'] = node.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['published'] = None
            parsed_content.append(parsed_item)
        return parsed_content


class GoogleParser(AbstractNewsParser):
    def get_url(self) -> str:
        return 'https://news.google.com/news/feeds?output=atom'

    def parse_content(self, content: str) -> List[Dict[str, str]]:
        parsed_content = []
        dom = parseString(content)
        for node in dom.getElementsByTagName('entry'):
            parsed_item = {}
            try:
                parsed_item['title'] = node.getElementsByTagName('title')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['title'] = None
            try:
                parsed_item['content'] = node.getElementsByTagName('content')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['content'] = None
            try:
                parsed_item['link'] = node.getElementsByTagName('link')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['link'] = None
            try:
                parsed_item['id'] = node.getElementsByTagName('guid')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['id'] = None
            try:
                parsed_item['published'] = node.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue
            except IndexError:
                parsed_item['published'] = None
            parsed_content.append(parsed_item)
        return parsed_content
