import os
from threading import Thread
from urllib.parse import urljoin
from urllib.request import urlretrieve
import httplib2
from bs4 import BeautifulSoup
from patterns.singleton.singleton import Singleton


class ImageDownloaderThread(Thread):
    """A thread for downloading images in parallel."""

    def __init__(self, thread_id: int, name: str, counter: int) -> None:
        super().__init__()
        self.name = name

    def run(self) -> None:
        print('Starting Thread', self.name)
        download_images(self.name)
        print('Finished thread', self.name)


def traverse_site(max_links: int=10) -> None:
    """Parse a given site."""

    link_parser_singleton = Singleton()

    while link_parser_singleton.queue_to_parse:
        if len(link_parser_singleton.to_visit) == max_links:
            return

        url = link_parser_singleton.queue_to_parse.pop()

        http = httplib2.Http()
        try:
            status, response = http.request(url)
        except Exception:
            continue
        if status.get('content-type') != 'text/html':
            continue
        link_parser_singleton.to_visit.add(url)
        print('Added', url, 'to queue')

        bs = BeautifulSoup(response)
        for link in BeautifulSoup.findAll(bs, 'a'):
            link_url = link.get('href')
            if not link_url:
                continue

            link_parser_singleton.queue_to_parse = [link_url] + link_parser_singleton.queue_to_parse


def download_images(thread_name: str) -> None:
    """Provide image downloader."""

    singleton = Singleton()
    while singleton.to_visit:
        url = singleton.to_visit.pop()
        http = httplib2.Http()
        print(thread_name, 'Starting downloading images from', url)

        try:
            status, response = http.request(url)
        except Exception:
            continue

        bs = BeautifulSoup(response)
        images = BeautifulSoup.findAll(bs, 'img')

        for image in images:
            src = image.get('src')
            src = urljoin(url, src)
            basename = os.path.basename(src)

            if src not in singleton.downloaded:
                singleton.downloaded.add(src)
                print('Downloading', src)
                urlretrieve(src, os.path.join('images', basename))
        print(thread_name, 'finished downloading images from', url)
