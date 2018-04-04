from abc import ABC, ABCMeta, abstractmethod
from bs4 import BeautifulStoneSoup


class Parser(ABC):
    """An abstract product that represents parser to parse web content.
    One of its subclasses will be created in factory methods.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, content: str):
        pass


class HttpParser(Parser):
    def __call__(self, content: str) -> str:
        filenames = []
        soup = BeautifulStoneSoup(content)
        links = soup.table.findAll('a')
        for link in links:
            filenames.append(link.text)
        return '\n'.join(filenames)


class FTPParser(Parser):
    def __call__(self, content: str) -> str:
        lines = content.split('\n')
        filenames = []
        for line in lines:
            splitted_line = line.split(None, 8)
            if len(splitted_line) == 9:
                filenames.append(splitted_line[-1])
        return '\n'.join(filenames)

