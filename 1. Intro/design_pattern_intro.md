Design Pattern
- well known solution to recuring problems
- widely accepted by software developments community

Creational -> Polymorphisum 
eg: butterfly life cycle
- Singelton
- Factory 

Stuctural -> Inheritance
eg: DNA stucture

Behavioural -> methods
- observer
- visitiors

# Attributes:
- represent property of an entity
- capture the state of entity 

# methods:
- Represents behaviours
eg, participant, age, cancel_reg()

# Design pattern 
- developing software same problems appears again and again 
- common problems imply that there is always a established solutions
- design pattern are well known solutions for recuring problems
- widely accepted by software developments community
- no need to invent a wheel as there is already perfect solutions 
- systemetic reuse of best design ideas
- Lower cost and higher quality 
- creator by cristopher allexendar 

# characteristics
- Language Neutral
- design pattern are dynamic always new one coming up 
- design pattern are intentionally incomplete to promote customization
- professional software developer should master design patterns 

# Design pattern Types:
1. Creational
  - use - create objects systemetically 
  - benifits - flexibility
  - eg: different subtypes of objects from the same class can be created
        at runtime when you use creational patterns.
2. structural
  - use: Establish relationships between software components in particlar setiing or configurations
  - goal is to satisfy functional and nonfunctional requiremnts.
  - Functional requiremnts refer to what software does
  - nonfunctional requiremnts are how well it completes its job.
  - the question of how fast or slow software functions belongs to nonfunctional domains.
  - different requiremnts lead to various stuctures. implemnted stuctural patterns
3. behavioural
- use:
- how you make your objects interact with each others
- accompolish both functional and nonfunctional requiremnts.
- Focous:
- defining protocols between these objects when trying to work together. to accompolish
  a common goal.

# Summary
- some core object oriented mechanisums or concepts are foundation for developing design patterns
  whether creational, stuctural, behavioural, in the creation patterns polymorphisum is often in use.
  stuctural pattern take advantages of inheritance a lot. behavioural patterns heavily used methods and there signatures.

# across creational, stuctural, and behavioural patterns
interfaces are at work across all these different types of design pattern

# Understanding oops
- Core Concepts:
oops is mainstream software developemnts methodology today and many modern programing
languages support object oriented programing including python design pattern require
the use of objects oriented programing, deisgn pattern are irelevant to the non objects
oriented programing languages. such as C. 
understanding core conects of oops involve learning concepts such as objects and classes.

# objects:
Represents entities in both problems and solution domains
-------------
Environments ----> Entites interacting with the software
 Software ---> components
-----------
In other words, when you are building a piece of software you need to have components 
represnting all the moving pieces of your solutions. in addition you need to repesents
all these entities, interacting with the software in the problem. domain,
EG: take a confrence registration systems in this senario you can think confrence 
participants as being the problem domains
the registtration form partcipants are using is in the solution domain
you need both represented in your software.

# classes
- classes our templates used to create objects to avoid recreating them each time.
- think classes as cookie cutters for replicating the objects
- classes defined objects in terms of attributes and behaviours.

# attributes
- attributes represents the properties of an entity attributes.
- attribute also captures the current state of entity.

# Methods
- represents behaviours
- participant, age, cancel_reg()

Example - Regitration system of confrenece:
partcipants have - attributes: age
partcipants have - behaviour: cancel the registraion 
understanding the concepts like classes and objects is critical in object oriented programing

# Inheritance:
- Inheritance Establishes a relationship between two classes as parent and child
  # child class
  - keep all the attributes and methods of its parents
  - add new attributes and methods of its own
  - overrides the existing methods of its parents.
  eg: pet(name, newAttr, speak()) class with 2 child class dog
  and cat they are inheriting from pet class.
  however child class is overide speak methods and defination, the dog overirde speak methods
  to produce berking sound, cat overide to create meow sound

# Polymorphism
- Relies on Inheritance
- allow child classes to be instantiated and treated as the same type as their parents.
- In other words polymorphium enables a parent class to be a placeholder for its child
  classes.

Example:
- user of pet class
let say that you are coding the pet class and you want to let users to choose if their pet
objects will be dog or cat during runtime. this situations warrants using polymorphisum
if the object is dog it would make oops sound. if cat objects the meow sounds

# pattern context:
you need to know context in which the design pattern works best
the pattern context consist of the following
- Participants
  refer to classes involved to form a design pattern
  play differnt role to accomplish the goals of design patterns

- Quality attributes
  refer to non functional requiremnts - usability, modifiability, relability
  performance and more.
  quality attributes have impact on the entire software and architectural solution address them.

- Forces
  are various factors and tradeoff to consider when try to adapt particular design patterns
  qulaity attribute manifest forces
  unintended consiqunces

- consequnces
you are likely to end of facing some unintended consequnces. these consequnces could be
worse performance,
ultimate responsibility really falls on decision makers. who are expected to choose a 
design pattern after throughly considering its consequnces. knowing when to use a design
pattern and when not to use it, is crucical especially they can cause more problems
than solving them, when they are missused.

# working with pattern language:
the process of mastering terms used to describe design patterns is like learning a new language
therefore, we can safely say that these terms consitute a pattern language. tha pattern language
consist of name, context, problem, solution and related patterns
- Name
  . capture gist of each patterns and these name becomes an essentail part of vocabulary during      design process Therfore pattern name needs to be especially meaningful and memorable
- Context
  . provides a senario in which we may use this patterns, it also offer inside when to use patterns
- Problem:
  . the problem part of pattern language descibes a design challanges a pattern is trying to address.
- Solution:
  . specifies the pattern itself. pattern are specified in term of stucture and behaviours
  . the stucture in case specifies the relationships between the elements used in patterns.
  . the behaviour specify all the instructions between the pattern elements.
- Related pattern
  . the last part of pattern language is related patterns. this list other pattern used together
    with pattern being descibed or similar patterns. In these related patterns section of pattern
    language its crucical to percisely describe the subtle differences between the pattern 













