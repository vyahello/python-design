from patterns.proxy.subjects import ProxySubject

if __name__ == '__main__':
    proxy1 = ProxySubject()
    proxy2 = ProxySubject()
    proxy3 = ProxySubject()
    proxy1.sort(reverse=True)
    print('Deleting proxy2')
    del proxy2
    print('Other object are deleted upon program termination')
