from abc import ABC, ABCMeta, abstractmethod
from typing import List
import random


class AbstractSubject(ABC):
    """A common interface for real and proxy objects."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def sort(self, reverse: bool=False) -> List[float]:
        pass


class RealSubject(AbstractSubject):
    """A class for a heavy object which takes a lot of memory space and takes some time to instantiate."""

    def __init__(self) -> None:
        self._digits = list()

        for i in range(10000):
            self._digits.append(random.random())

    def sort(self, reverse: bool=False) -> List[float]:
        if not reverse:
            self._digits.sort()
        else:
            self._digits.reverse()
        return self._digits


class ProxySubject(AbstractSubject):
    """Proxy has the same interface as RealSubject."""

    reference_count = 0

    def __init__(self) -> None:
        """A constructor which creates an object if it is not exist and caches it otherwise."""

        if not getattr(self.__class__, 'cached_object', None):
            self.__class__.cached_object = RealSubject()
            print('Cached new object')
        else:
            print('Using cached object')
        self.__class__.reference_count += 1
        print('Count of references = ', self.__class__.reference_count)

    def sort(self, reverse: bool=False) -> List[float]:
        """The args are logged by the Proxy"""
        print('Called sort method with args:')
        return self.__class__.cached_object.sort(reverse=reverse)

    def __del__(self):
        """decreases a reference to an object, if the number of reference is 0, delete the object"""
        self.__class__.reference_count -= 1

        if self.__class__.reference_count == 0:
            print('Number of reference_count is 0. Deleting cached object...')
            del self.__class__.cached_object
        print('Deleted object. Count of objects = ', self.__class__.reference_count)
