import os
from urllib.parse import urlparse
from patterns.singleton.image import ImageDownloaderThread, traverse_site
from patterns.singleton.singleton import Singleton


if __name__ == '__main__':
    root = 'http://python.org'
    parsed_root = urlparse(root)
    singleton = Singleton()
    singleton.queue_to_parse = [root]
    singleton.to_visit = set()
    singleton.downloaded = set()

    traverse_site()

    if not os.path.exists('images'):
        os.makedirs('images')

    # Create new Threads
    thread1 = ImageDownloaderThread(1, "Thread-1", 1)
    thread2 = ImageDownloaderThread(2, "Thread-2", 2)

    # Start new Threads
    thread1.start()
    thread2.start()
