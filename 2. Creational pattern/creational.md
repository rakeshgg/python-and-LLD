# Factory
- Factory encaptulates objects creations
- that is factory is an object. specializing in creating other objects
- the factory pattern is useful specially when you are not sure about what type of
  objects you will be needing eventually in your system another possibility is that
  your application need to decide on what class to use at runtime
Senario we are using
- pet shop originally selling only dogs
- now you need to sell cats too therfore your system needs to handle cats as well as dogs
- it supposed to show how each pets you sell to speak

# Abstract factory Methods
- abstract factory build on factory patterns
- Abstract factory is useful when user exceptions yields multiple related objects.
- except to receive Family of related objects at a given time but doesnot have to know
- which family it is until runtime.
Senario we are using
Dog Factory - Dog, Dog Food
Cat Factroy - Cat and Cat Food

we first build a pet factory whose concerte factories include dog factory and cat factory
both dog and cat factory produces dogs and cats. as well as related products such as
dog food and cat food

Solution:
In Theory our solution abstract factory consists of abstract factory, concrete factory, abstracts products and concrete products. for the abstract factory we use pet factory. for concrete factory 
we use dog factory and cat factory. and finally for concrete products we'll creating dogs, the type
of pet and dog food. cat and cat food
- Abstarct Factory - pet factory
- Concrete Factory - dog factory and cat factory
- Concrete products - dog and dog foods, cat and cat foods.
We implemnt our abstract factory without using inheritance because python is dynamically typed
language, and therefore doesnot required abstract classes. Abstarct factory is related to the
factory patterns in the sense that it creates the objects concrete factories are often single terms

# Singleton Patterns:
Accroding to Gang of four defination, singleton is the pattern you need when you want
to allow only one objects to be created from class its and object oriented way of providing
global variables
- Global variable in an object oriented ways
- Borg, unlike singelton borg allows multiple objects instances but they all share the same state.
  which meansa same objects values in the objects.
- Borg is a short for cyborg prominantely featured in the star trek series.
  they share collective dots like objects in the python borg patterns

Senario:
why you need a pattern like singelton or Borg?
object1, object2, object3 --> cache
Lets say there is need of keeping a cache of information to be shared by various
elements of yourself in the system by keeping this information in a single objects
like Singelton or sharing it constantly on borg objects there is no need to retrieve
the information from its original source each time

Solutions:
All module in python acts as singelton
- module - shared by multiple objects
in our senario borg acts as information cache for netwroking acroynms, and there
spelled out versions
- Borg design patterns - computer network acronyms, spelled out versions

# Builder patterns
- Builder is solution to an anti-pattern called telescopic construction
- anti pattern is opposite of best programing practices. and what we want to avoid
- The telescopic constructors anti-pattern occurs when software developer attempt to
  build a complex objects. using an excessive numbers of constructors.
- The builder pattern is trying to solve this problems
Senario:
Think of senario in which you are trying to build a car this test requires
various car parts(tires, engine) to be first constructed Individually and 
than assembled. the builder pattern brings order to this chaotic process
Solution
to remove unnecsssary complexity as possible it partions the process of building
a complex object into four different role. the first role is the director
in charge of actually building the products. the second role to provide
all necessary interfaces required in buiding an objects. we call this one as
Abstarct builder because there'll be a concrete builder inheriting from it.
the concerte builder class inherit from the abstract builder class and actually
implemnts the details of interfaces of the abstract builder class. for the 
specific type of products the products role repersents an objects being built
The builder pattern doesnot rely on polymorphisum unlike factory and abstract
factory
The Focus of builder pattern is instead on reducing the complexity of building
an elaborate objects. through divinde and conqure strategy
- Director
- Abstarct Builder - interfaces
- Concrete builder - Implemnts the interfaces
- Product - object being built

# Prototype patterns:
Prototype clones objects according to a prototypical instances
here the keyword is cloning. note that we are taking about making
a copy instead of building prototype is useful when instantitaing
many identical objects individually which could be expensinve in 
term of computing power.
cloning could be a good alternatives beacuse it makes a carbon copy
in the memory space instead of building individual objects.
respectively from scratch the usual way

Scanrio:
Lets assume we are building a car we can mass produce car more easily and quickly
if the cars have same colors and options. similarly in python programing
scanrio you can clone objects by making copy of prototype objects insted of 
building them through constructors as long as they are supposed to be 
identical without variations

# solution
our solution consist of creating a prototypical instances first
and then cloning it whenever you need the replica the pattern related to
the prototype pattern is the abstract factory.





