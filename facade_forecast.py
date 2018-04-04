from patterns.facade.weather.facade import Facade

if __name__ == '__main__':
    facade = Facade()
    print(facade.get_forecast('London', 'UK'))
