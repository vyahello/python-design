from patterns.command.commands import LsCommand, TouchCommand, RmCommand
from patterns.command.invoker import Invoker
from patterns.command.receivers import LsReceiver, TouchReceiver, RmReceiver

if __name__ == '__main__':
    ls_command = LsCommand(LsReceiver())
    touch_command = TouchCommand(TouchReceiver('test_file'))
    rm_command = RmCommand(RmReceiver('test_file'))

    file_commands = [ls_command, touch_command, rm_command]

    invoker = Invoker(create_file_commands=file_commands, delete_file_commands=file_commands)
    invoker.create_file()
    invoker.delete_file()
    invoker.undo_all()
