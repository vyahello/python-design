from patterns.observer.observers import USATimeObserver, EUTimeObserver

_timestamp = 0.1
_usa_name = 'USATimeObserver'
_eu_name = 'EUTimeObserver'


def test_usa_time_observer():
    assert USATimeObserver(_usa_name).notify(_timestamp) == 'Observer USATimeObserver says: 1970-01-01 03:00:00AM'


def test_eu_time_observer():
    assert EUTimeObserver(_eu_name).notify(_timestamp) == 'Observer EUTimeObserver says: 1970-01-01 03:00:00AM'
