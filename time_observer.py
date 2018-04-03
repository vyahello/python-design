from patterns.observer.observers import USATimeObserver, EUTimeObserver
from patterns.observer.subject import TimeSubject
import time

if __name__ == '__main__':
    subject = TimeSubject()
    print('Adding usa_time observer')

    observer1 = USATimeObserver('usa_time_observer')
    subject.register_observer(observer1)
    subject.notify_observers()

    time.sleep(2)
    print('Adding eu_time observer')
    observer2 = EUTimeObserver('eu_time_observer')
    subject.register_observer(observer2)
    subject.notify_observers()

    time.sleep(2)
    print('Removing usa_time_observer')
    subject.unregister_observer(observer1)
    subject.notify_observers()
