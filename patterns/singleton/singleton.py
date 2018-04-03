from typing import Any


class Singleton(object):
    """Represent a singleton object."""

    def __new__(cls) -> Any:
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
