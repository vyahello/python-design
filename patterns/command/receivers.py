import os


class LsReceiver(object):

    def show_current_dir(self):
        """The receiver shows how to execute the command"""

        cur_dir = './'
        filenames = []
        for filename in os.listdir(cur_dir):
            if os.path.isfile(os.path.join(cur_dir, filename)):
                filenames.append(filename)
        print('Content of dir: ',  os.path.join(' '.join(filenames)))


class TouchReceiver(object):
    def __init__(self, filename: str):
        self._filename = filename

    def create_file(self):
        """Actual implementation of unix touch command."""
        with open(self._filename, 'a'):
            os.utime(self._filename, None)

    def delete_file(self):
        """Undo unix touch command. Here we simply delete the file."""
        os.remove(self._filename)


class RmReceiver(object):
    def __init__(self, filename: str):
        self._filename = filename
        self._backup_name = None

    def delete_file(self):
        """Deletes file with creating backup to restore it in undo method."""
        self._backup_name = '.' + self._filename
        os.rename(self._filename, self._backup_name)

    def undo(self):
        """Restores the deleted file."""
        original_name = self._backup_name[1:]
        os.rename(self._backup_name, original_name)
        self._backup_name = None
