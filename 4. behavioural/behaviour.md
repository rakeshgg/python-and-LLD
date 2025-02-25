# Observer pattern
- The observer pattern establishes one to many relationship
  between subject and multiple observers.
- our problem is here that a subject need to be monitored
  and other observer objects should be notified when there is
  change in the subject.
Scenario:
we keep track of the core temperatures of reactors at a power plant
when there is change in core temperature resiterd observer must be notified
Solution:
our solution uses an abstarct class called subject which has the interface
that allows operations such as attaching deteching and notifying observers
Attach, Detach, Notify
we also need concrete subject classes Inheriting from the abstract subject classes.
Singelton is related to observer design pattern.

# Visitor Pattern
Visitors allow adding new features to an existing class
hierachy without changing it
problems:
- some time necessary to add new operations
- dynamically to Existing classes
- with minimal chnages
Senario:
- House class
- HVAC Specialist - visitor type 1
- Electrician - visitor type 2
Solution:
The visitor patterns represents new operations to be
performed on the various elements of an exiting class
hierachy
Visitors can also provide operations on a composite
object.

# Iterator pattern
- The iterator pattern allows a client to have sequntial access to the elements
  of an aggregate objects without exposing its underlying stucture
- The problem is that some programers overcrowd the traversal interface
  of an aggregate objects. for every possible ways of iteration
Scenario:
we'll building our own iterator that takes advatages of build in python iterator
called zip
The iterator goes through a list of german counting words. It will iterate only up
to certain point. based on client input The iterator isolates access and travesal 
features from the aggregate objects. it also provide an interface for accesing 
the elements of an aggreaget objects an iterator keep track of the obejct being
traversed. our solution is to make aggregate objects create an iterator for client
The composite design pattern is realted to the iterator pattern
Solution:
Isolation, Interface, Tracking, Recommendation

# Strategy patterns:
The strategy pattern offers a family of interchangable algorithum to the client
Problem:
The problem we often see is that there is a need for dynamically
changing the behaviour of an objects.
We offer our strategy class with the default behaviour
when there is need we provide another variation of the strategy class by dynamically
replacing its default method with new one
Solution
python allows adding methods dynamically by importing the types module

# chain of Responsibility patterns
chain of Responsibility patterns opens of various possibilities of processing
for a given request. The chain of responsibility pattern decouples the request
and its processing Our problem is that many different type of processing need to
be done depending on the request.
Scanrio:
in our scanario we receive the integer value we use different handlers
to find out its range as our solution, we use abstract handler that stores
a successor that will handle a request. if the current handaler doesnot
handle it. concrete handler check if they can handle the Request if they
can, they handle it and return true value, indicating that the request
was handled. Composite is related to the chain of responsibility patterns
Solution
- Abstract Handler - successor
- Concrete handler - checks if it can handle the request








