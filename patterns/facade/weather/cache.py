from datetime import timedelta, datetime
import pickle


class Cache(object):
    def __init__(self, filename: str) -> None:
        self._filename = filename

    def save(self, obj) -> None:
        with open(self._filename, 'w') as file:
            dct = {
                'obj': obj,
                'expired': datetime.utcnow() + timedelta(hours=3)
            }
            pickle.dump(dct, file)

    def load(self) -> None:
        try:
            with open(self._filename) as file:
                result = pickle.load(file)
                if result['expired'] > datetime.utcnow():
                    return result['obj']
        except IOError:
            pass
