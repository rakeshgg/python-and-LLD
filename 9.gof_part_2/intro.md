# mediator Pattern
Imagine a bueasy airport where airplabes are waiting and moving on various runway
piolts talk to each other and avoid collisions on their own but this will be impossible
task due to complexity of the problem. as well as their inability to see the big pictures
This is why we need a mediator such as an airtraffic controller to centerally and effectively
manage the communication among the individuals pilots.

A similar sceanrio can occurs in programing when there are too many
objects interacting with each other, individually the complexity
of code can increase dramatically. and its maintainbility also
decreses. In particuar a simple change in one object can have a huge ripple
effect on the rest of the code we call this phenomena as tight coupling
among objects. 
   A logical solution to this problem is creating and designating an object
as mediator for other objects. the mediator pattern is the design pattern
community answer to implementing this solution. as its name suggest, a
mediator is a behavioural pattern the pattern consit of mediator class
and its colleague classes. the colleauge classes do not communicate
with each other directly and therfore not coupled stronlgly. Note that
the respective relationship among the colleague objects are embodied
In the mediator class This eliminates otherwise complex communication
that could be resulted from the many to many message exchnages
among the collegue objects.

In summary when you need to promote the loose coupling
between your objects and increase their maintanibility
the mediator pattern is a perfect design solution for you.

# Memento
To revert and action when using a system
undo shortcut in our wordprocessing programs
In case of db applications rollback is an essential
options. because irreversible changes can do humongous
damage to both your task at hand. and future objectives
if you are looking for design solution to this type of programing need
Memento is perfect behavioural design pattern for you. This pattern 
allows you to capture the internal state of an object at a creatain
points of time and restore same state later in future if necessary
An object can take on this task in addition to its core mission, but this
will make it bulkier and more complex. A betetr solution is to introduce the
new obejct dedicated to storing the history. of transaction associated with
the other obejct.
Note that the goal is here is not to store every single property
of a target object, but to get only those relevant to your undeo operations
momento pattern uses three classes. two accomplish its task.

the momento class is responsible for storing the internal state information
of an object. In addition the memento class has interface available to the 
originator class. orginator create a Memento obejcts to capture the internal
state of an obejcts. it also uses same Memento object to restore the previous
state. caretaker maintains the memento objects and doesnot have direct access
to its interface. memento organises your code efficiently by seperating the
programing tasks of maintainig object state from capturing and restoring operations

Orginator(state, setMemento, CreateMemento) -> Memento(state, GetState, setState) <----> Caretaker

# state
There are many amazing things happening around us. all the time even in real life 
situtations 
The metamorphics of an insects comes to mind. think of dragonflies. they spend most of their
...
in the word of oops programing we also run in similar situations. Imagine a senario
in which you need to transform objects, specially in term of their behaviour
when there internal state changes.
For Example an automatic teller machine or ATM need to exibits
different behaviour when its internal state changes. on such senario
when it runs out of money, Normally atm despenses the money if user provides
appropriate cred and resonable money amount.
same ATM machine behaves differently when there is no money
it will diaply a warning message to the user and say that it is out of money.
state design pattern offers behavioural design solutions to accomodate
this types of pograming needs. The pattern has the state class
which is extend by its child class it representing a different state in which an obejct
can find itself. The context class is what a client interact with to set state and
its behaviour. 
If i was asked to programe a particular super hero my choice of design pattern
would ofcourse be the state. 

# Tempelate methods
Inheritance allow a child class override methods defined by its parent class.
This capability is refered to as polymorphisum for eg: the parent class shape here
has a draw method. which can overriden by its child class. such as triangle, rectangle,
circle.
when i execute the draw methods the triangle class it will draw triangle.
The template method pattern is behavioural in nature provide strict version of 
polymorphisum.
it allows or forces only a select group of methods. to be overriden an prevents
the rest. of methods belonging to parent class from being changed by its child
classes. 
by resticting how much child classes can deviate from it's parent class
The template method pattern defines a skeleton of operations that will
be always present in child classes it is solution that allows developers
to extract commonalities across similar classes. and to place them into
a class whose template methods offers common interfaces
help to avoid widesperd changes. 
Frameworks adopt template methods for the obvious purpose. of keeping
the control over what can be customized by its users and what need to
stay the same across the board.
The Framework called the shots instead of it's adopters.




