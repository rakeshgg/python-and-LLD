# Facade
do you know all inner working of car when you drive one?
you start a car by interacting directely and individually with
your starter motors. fuel pump, ignition, battery, and finally
your engine. as we know very well there is no need to do this
and all that required a push of buttons or turn your car key.
The more you hide the unnecessary details, the better. the
same priciple applied to the concept of facade. tha pattern hides
the nonessential details. of the individual interfaces of systems
That compromise a complesx system such as compiler facade is a stuctural
patterns and consists of a facade class and set of subsystem it
represnts. through its own simple and unified Interface This way the
users of the Facade interface don't have to know all the details
of the subsystem interfaces to use there functionality. the before and
after diagram shows here demonstrates the different facade makes 
intutively. In addition to the obvious and imediate benifits of
reducing complexity. facade can also protects its client classes.
from the changes in the susbsytem interfaces this is because
facade can hide the susbsystem modifications behind itself and therfore
keep its own interface as stable as possible.

- Reduce complexity
- protects client classes.
- promotes loose coupling between client and subsystem.
- Increases maintainability of the system as whole. using the facade pattern doesnot
prevent the option of accesing the subsystem classes directely programmers still keep
the flexibility of having full visibility to more complex susbstem interfaces.

# Command
- There are situations when its's necessary to wrap a request in an object.
oopps like language python the requests come in the form of a method.
The command pattern address this need and provides guidance on how to best
build an object. whose sole purpose is to package a method that can be easily
passed around.

Client -------> Invoker --------> Command|+Execute()
|                                            |
|                                            |
-------- Receiver|+Action() <---------- concreteCommand|-state, +Execute
                              receiver              |
                                                    |
                                                    Receiver Action()

command provide interface to execute a methods. users of the command pattern write there own concrete commands, which inherit from command class. one of the resion you need to encaptulates a method is to delay or queue the execution of an action. on a receiver objects.
This capability is specially useful when you need to dynamically compose a sequence
of behaviour or undo actions. the word encaptualtes here is a fancy way of saying
wrapping to reitrate the concrete command are our mechanisum for invoking an action
on a receiver objects. it implements the execute interface of command class. A client
objects initiates a transaction involving a concrete command by creating a concrete
command objects and deciding who its receiver is The invoker class is resposible
for holding onto various commands objects and telling them to take an action
on a receiver when the time is right. the comamnd pattern has many practical 
uses. you may be pleasently surprised by how often you find the relevent
in your daily coding situations. once you understand the concept of 
and motivation behind the patterns

Why use command pattern
- Compose behaviour
- Undo actions

# Interprter example
- Expert in a particular fields often develop their own language called
  a domain-specific language they use special terms to refer to certain
  concepts. this allow them quickly convey what need to be communicated
  without needing to explain the details every time. 
  The interpreter pattern makes it possible to use. this kind of domain specific
  language. to perform a task in your computer make this happens your computer need
  Interprter language that transalte into expression.
  Interpreter design pattern provides clever design guidance

  Client ----> Context
      |
      --------> AbstractExpression(Interpreter(Context))---
                    |                                     |
        |--------------------------|                      |
    Terminal Expression         NonTerminalExpression =====
    Interprete(context)          Interprete(context)

 Terminal Expression  - End of exprssion
 NonTerminalExpression - 

 # UML.org - Unified modelling language
 - class diagram
 - Sequnce diagram
 A sequence diagram specifies the behaviour of objects once they get
 instantiated from classes !.e creating new objects out of class.

 start UML