# Python Design Patterns
Inspired by Packt book - [Learning Python Design Patterns](https://www.packtpub.com/application-development/learning-python-design-patterns) that describes popular design patterns in python.

## Singleton
Singleton is a design pattern that allows to create only one instance of an object.

Please run `web_crawler.py` program to download images from web sources.
```bash
~ python web_crawler.py
```
### Classic Singleton.
Allows to create one unique object. All other instances will be the same.

### Borg Singleton
All instances are distinguished but remain the same state and behaviour.

**Note**: modules in python are singletons.

## Factory
Factory is class for creating other classes.

Please use `factory_web_access_v1.py`, `factory_web_access_v2.py` and `factory_method_web_connector.py` programs to instantiate Http(s), Ftp(s) connections.

```bash
~ python factory_web_access_v1.py
~ python factory_web_access_v2.py
```
### Factory method
Factory method defines an interface for creating an object. Makes code tied not to concrete classes but to interfaces.

### Abstract factory
Abstract factory provides interface for creating families of related objects. Is used when you need to create a family
of objects that do some work together. Abstract factory is used to define the interface of factories (methods).
Benefit - isolates the creation of objects from client, giving client possibility to access them via interface.

## Facade
Facade is a design pattern that provides unified interface instead of a set of interfaces. Used when it is needed to 
provide a simpler interface to a complex subsystem. All interaction with the client goes through the Facade. 
All dependencies are using inside the facade code but not related to client code.
For instance when you turn on pc , your OS hides all internal work of the pc because OS provides a simplified interface
to use the machine.

Please use `facade_foracast.py` tool allows to get weather from different zones:
```bash
~ python facade_foracast.py
```

## Proxy and Observer
### Proxy
Proxy is a design pattern that facilitates objects and is functioning as an interface of other class.
It helps to decouple the client code from the object that client code uses.
Mainly used when you need to defer initialising of an object until it is indeed necessary (it may occupy lots of memory).

Please use `proxy.py` program to delegate heavy tasks for other objects
```bash
~ python proxy.py
```

### Observer
Observer is a design pattern when you need to implement one-to-others relationship (convey the same information to 
multiple clients). It is kind of publish-subscribe pattern like in twitter when you post a tweet and all followers
will be notified.

Please use `time_observer.py` program to measure time for USA and EU timezones.
```bash
~ python time_observer.py
```

## Command
Command pattern is a great design pattern for unix type commands.
Provides an interface to perform some job and encapsulates all necessary info to do it in one object call.
Disadvantage - separate class for each individual command.

Please use `unix_commands.py` program to run simple unix commands.
```bash
~ python unix_commands.py
```

## Template method
Main idea is to create a method that will hold a sequence of steps (primitive operations).

Please use `news_parser.py` tool allows to parse top 3 news from google and yahoo sources.
```bash
~ python news_parser.py
```

Hook is method that can be defined in abstract class and can be overridden in concrete classes but not obligated to do it.
Hooks are used for small changes in an algorithm while avoiding code duplication.

### Run unittests
Run `pytest -v` from shell in the root directory of the repository.  

### Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all require python packages
