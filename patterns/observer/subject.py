from abc import ABC, ABCMeta, abstractmethod
import time
from patterns.observer.observers import Observer


class Subject(ABC):
    """Represent abstraction for specific subject."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unregister_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class TimeSubject(Subject):
    """Represent time subject."""

    def __init__(self) -> None:
        self._observers = list()
        self._ctime = None

    def register_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            print(observer, 'already in subscribed observers')
        else:
            self._observers.append(observer)

    def unregister_observer(self, observer: Observer) -> None:
        try:
            self._observers.remove(observer)
        except ValueError:
            print('No such observer in subject')

    def notify_observers(self) -> None:
        self._ctime = time.time()
        for observer in self._observers:
            observer.notify(self._ctime)
