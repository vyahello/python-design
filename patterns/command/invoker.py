from typing import Iterable
from patterns.command.commands import Command


class Invoker(object):
    def __init__(self, create_file_commands: Iterable[Command], delete_file_commands: Iterable[Command]):
        self._create_file_commands = create_file_commands
        self._delete_file_commands = delete_file_commands
        self._history = []

    def create_file(self):
        print('Creating file...')
        for command in self._create_file_commands:
            command.execute()
            self._history.append(command)
        print('File created. \n')

    def delete_file(self):
        print('Deleting file...')
        for command in self._delete_file_commands:
            command.execute()
            self._history.append(command)
        print('File deleted.\n')

    def undo_all(self):
        print('Undo all...')
        for command in reversed(self._history):
            command.undo()
        print('Undo all finished.')
