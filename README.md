# Python Design Patterns

## Singleton
Singleton is a design pattern that allows to create only one instance of an object.
1. Classic Singleton.

Allows to create one unique object. All other instances will be the same.

2. Borg Singleton

All instances are distinguished but remain the same state and behaviour.

Note - modules in python are singletons.

## Factory
Factory - class for creating other classes.

1. Factory method

Factory method - defines an interface for creating an object. Makes code tied not to concrete classes but to interfaces.

2. Abstract factory

Abstract factory - provides interface for creating families of related objects. Is used when you need to create a family
of objects that do some work together. Abstract factory is used to define the interface of factories (methods).
Benefit - isolates the creation of objects from client, giving client possibility to access them via interface.

## Facade
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
                                            
client -> Facade: do_some() -> facade uses 3 submodules inside, call them and returns some response to 
the client (via do_some()), client doesnt need to know about this 3 modules.
it can just call the Facade and receive what it wants. Using decomposition principle break down complex system 
into small subsystems
```

## Proxy and Observer
1. Proxy

Proxy is a design pattern that facilitates objects and is functioning as an interface of other class.
It helps to decouple the client code from the object that client code uses.
Mainly used when you need to defer initialising of an object untill it is indeed necessary (it may occupy lots of memory).
```
UML diagram

                                                    <<interface>>
                                                       Subject
                                                      do_some()
                                          ________________|_________________       
                                          |                                |
                                          
Client --uses--> Proxy: do_some()--delegates-> RealSubject: do_some()

Proxy and RealSubject are inherited from the same interface - Subject.
Client uses Proxy which delegates calls to RealSubject object.
```
2. Observer

Observer is a design pattern when you need to implement one-to-others relationship (convey the same information to 
multiple clients). It is kind of publish-subscribe pattern like in twitter when you post a tweet and all followers
will be notified.

## Command
Command pattern is a great design pattern for unix type commands.
Provides an interface to perform some job and encapsulates all necessary info to do it in one object call.
Disadvantage - separate class for each individual command.

```
UML diagram

                                                          <<interface>>
                                        Invoker-----calls-->Command: execute()
                                                                |
                                        Client-----creates->ConcreteCommand: execute()--delegates-->Receiver: do_work()

Invoker calls execute() of an object with Command interface. It is object of ConcreteCommand class in which the execute method calls an object of the Receiver
that does some work.
```

## Template method
Main idea - create a method that will hold a sequence of steps (primitive operations).

```
UML diagram


                                        ABC: template_method(), primitive_oper1(), primitive_oper2() - template_method(), primitive_oper1(), primitive_oper2()
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
