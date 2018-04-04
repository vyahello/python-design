from abc import ABC, ABCMeta, abstractmethod
from patterns.command.receivers import LsReceiver, TouchReceiver, RmReceiver

_history = []


class Command(ABC):
    """The command interface"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self) -> None:
        """Method to execute the command"""
        pass

    @abstractmethod
    def undo(self) -> None:
        """A method to undo the command"""
        pass


class LsCommand(Command):
    """Concrete command that emulates ls unix command behaviour"""

    def __init__(self, receiver: LsReceiver = LsReceiver()):
        self._receiver = receiver

    def execute(self) -> None:
        """The command delegates the call to its receiver"""
        self._receiver.show_current_dir()

    def undo(self) -> None:
        """Can not undo ls command"""
        pass


class TouchCommand(Command):
    """Concrete command that emulates touch unix command behaviour."""

    def __init__(self, receiver: TouchReceiver):
        self._receiver = receiver

    def execute(self) -> None:
        self._receiver.create_file()

    def undo(self) -> None:
        self._receiver.delete_file()


class RmCommand(Command):
    """Concrete command that emulates rm unix command behaviour."""
    def __init__(self, receiver: RmReceiver):
        self._receiver = receiver

    def execute(self) -> None:
        self._receiver.delete_file()

    def undo(self) -> None:
        self._receiver.undo()
