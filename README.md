# Python Design Patterns
Inspired by Packt book - "Learning Python Design Patterns" that describes popular design patterns in python.

## Singleton
Singleton is a design pattern that allows to create only one instance of an object.
- `web_crawler.py` tool allows to download images from web sources.
```bash
~ python web_crawler.py
```
1. Classic Singleton.

Allows to create one unique object. All other instances will be the same.

2. Borg Singleton

All instances are distinguished but remain the same state and behaviour.

Note - modules in python are singletons.

## Factory
- `factory_web_access_v1.py` and `factory_web_access_v2.py` tools allow to instantiate Http(s), Ftp(s) connections
- `factory_method_web_connector.py` tool allow to instantiate web access via http(s), ftp(s)
Factory - class for creating other classes.

```bash
~ python factory_web_access_v1.py
~ python factory_web_access_v2.py
```
1. Factory method

Factory method - defines an interface for creating an object. Makes code tied not to concrete classes but to interfaces.

2. Abstract factory

Abstract factory - provides interface for creating families of related objects. Is used when you need to create a family
of objects that do some work together. Abstract factory is used to define the interface of factories (methods).
Benefit - isolates the creation of objects from client, giving client possibility to access them via interface.

## Facade
- `facade_foracast.py` tool allows to get weather from different zones.

Run `facade_foracast.py` tool
```bash
~ python facade_foracast.py
```

Facade is a design pattern that provides unified interface instead of a set of interfaces. Used when it is needed to 
provide a simpler interface to a complex subsystem. All interaction with the client goes through the Facade. 
All dependencies are using inside the facade code but not related to client code.
For instance when you turn on pc , your OS hides all internal work of the pc because OS provides a simplified interface
to use the machine.
```
UML diagram


                module1    module2    module3
                |            |           |
                --------------------------
                             |
                             |
                           Facade:
                          do_some()
                             |
                             |
                          do_some()
                             |
                           Client
                                            

```
Client -> Facade: do_some() -> facade uses 3 submodules inside, call them and returns some response to 
the client (via do_some()), client doesnt need to know about this 3 modules.
It can just call the Facade and receive what it wants. Using decomposition principle break down complex system 
into small subsystems.
## Proxy and Observer
- `proxy.py` tool allows to delegate heavy tasks for other objects

```bash
~ python proxy.py
```

- `time_observer.py` tool allows to  to measure time for USA and EU timezones.

```bash
~ python time_observer.py
```
1. Proxy

Proxy is a design pattern that facilitates objects and is functioning as an interface of other class.
It helps to decouple the client code from the object that client code uses.
Mainly used when you need to defer initialising of an object until it is indeed necessary (it may occupy lots of memory).
```
UML diagram

                         <<interface>>
                            Subject
                           do_some()
               ________________|_________________       
               |                                |
                                          
```
Client --uses--> Proxy: do_some()--delegates-> RealSubject: do_some().Proxy and RealSubject are inherited from the same interface - Subject.Client uses Proxy which delegates calls to RealSubject object.
2. Observer

Observer is a design pattern when you need to implement one-to-others relationship (convey the same information to 
multiple clients). It is kind of publish-subscribe pattern like in twitter when you post a tweet and all followers
will be notified.

## Command
- `unix_commands.py` tool allow to run simple unix commands.

```bash
~ python unix_commands.py
```

Command pattern is a great design pattern for unix type commands.
Provides an interface to perform some job and encapsulates all necessary info to do it in one object call.
Disadvantage - separate class for each individual command.

```
UML diagram

                              <<interface>>
              Invoker-----calls-->Command: execute()
                                      |
              Client-----creates->ConcreteCommand: execute()--delegates-->Receiver: do_work()

```
Invoker calls execute() of an object with Command interface.
It is object of ConcreteCommand class in which the execute method calls an object of the Receiver that does some work.
## Template method
- `news_parser.py` tool allows to parse top 3 news from google and yahoo sources.

```bash
~ python news_parser.py
```
Main idea - create a method that will hold a sequence of steps (primitive operations).

```
UML diagram


ABC:  template_method(),
|     primitive_oper1(),
|     primitive_oper2() - template_method(),
|     primitive_oper1(), primitive_oper2()
|
ConcreteClass: primitive_oper2()
```
Hook - method that can be defined in abstract class and can be overridden in concrete classes but not obligated to do it.
Hooks are used for small changes in an algorithm while avoiding code duplication.

## Contributing

### Setup
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vjagello93@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all require python packages

### Run unittests
Run `pytest -v` from shell in the root directory of the repository.  
