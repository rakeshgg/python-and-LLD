# Decorator pattern
The decorator design pattern is a stuctural pattern that allow users
to add new features to existing objects without changing the stuctures
pattern makes implemnting the decorator pattern very staringht forwards
due to its built in language features
problem:
- add additional features to an existing objects dynamically without using subclasses.

Senario:
we start a function diplaying a hello word message
you want to make message look fancier by decorating it with additional tasks
such as blink

Solutions:
Functions are objects in python and we can add additional features to these functions
using built in decorators in python pattern such as Adapter, composite, strategy
are related to decorator patterns.

# Proxy Design pattern
proxy becomes handy when creating a highly resource-intensive objects
The problem we need to solve here is postponing our object creation
as long as possible due to the high resource requirements of the objects
we are creating therfore there is need for a placeholder that will in turn
create the objects when its creation is absoulately necessary
Scenario:
We create an instances of produccer class only when its availble because only fixed
number of producer objects can exits at a given time. Our proxy is an artist who is
checking to see if the produccer become available for Guest
Solution:
In Proxy design pattern
client interact with proxy objects most of the time until the resource intensive
objects become available. the proxy objects in charge of creating the resource
intensive objects Adapter and decorator are related to the proxy design patterns

# Adapter patterns
- The adapter pattern converts the interface of a class into another one a
- client was expecting This time our problem is that the interfaces are incompatible
- between client and a server.
- In our senario we have Korean and british objects that have differnt methdos
name for speaking. The client is like to use a uniform interface that is the speak method

Solution:
our solution is use the adapter pattern that transalate the method names between the client
and the server code. bridges and decorators are related to adapter patterns

# composite design pattern
The composite design pattern maintains tree data stucture to represents
part-whole relationships. here we want to build a recursive tree data stucture
so that elements of tree can have its own sub-elements eg menu>submenu>sub-submenu
Scanrio:
An example of this problem is creating menu and sub-menu items the sub-menu items
can also have their own sub-menu items. our coding challanges is to diplay menu
and sub-menu items. using the composite design pattern
Solution:
our solution consist of three major elemnets. The First one is 
Component, the second one is child and third one is composite
The component elements is an abtract class or concrete class
called child, inherit from the componet class
And than we have another concrete class Composite which also
inherit from component class finally our composite class maintinas child
objects by adding and removing them to and from tree data stucture

# Bridge Patterns
The Bridge patterns help untangle an unnecsserirly complicated class hierachy
especically when implemnetaion specif class are mixed with Implementation 
Independet classes. The problem here is that
Problems:
There are two parallel orthogonal abstarctions
Unrelated, parallel or orthogonal abstractions
one implemnetation specific the other is implementaion 
Independet.
Senario:
- Implemenation Independet Circle absatrction involves defining the properties of circles
  and scaling it
- Implemenation dependet Circle absatrction involves how to draw a circle
Solution:
- Seperate abstarction into two different class hierachies
abstarct factory and adapter pattern are related pattern to bridge design pattern





