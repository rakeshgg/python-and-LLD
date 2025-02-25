Architetural patterns - MVC
Auality attributes- Performance, Security, maintainbility
Domin specif patterns
Gang of Four
- Command, Facade, Interpreter, Mediator, Memento, state, template methods

What is design pattern?
somebody already developed solution to your programing problems
if you have you're not alone in fact there are communites of 
people https://hillside.net/

design patterns are well know and documented solution to 
- Recuring challanges in oops envirnoments.

Types of Design patterns:
Creational - creational patterns are useful when you need to create an objects
            for a specifc purposes. 
            Singelton, Factory, Abstarct Factory, Builder, Prototype 
Stuctural - Assembles classes nad their instances
            Decorator, proxy, Adaptor, Composite, Bridge

Behavioural - pattern are common solutions to programing problems occuring
              when trying to effectively regulate communication among objects.
              - Regulate communication among objects.
              Observer, Visitor, Iterator, Strategy, chain of resposibility

# Architectural vs design patterns:
if you are not already familiar with Architectural patterns
 Design patterns:
  - Low level and concrete
  - are at class level
  - Address how classes are instantitated, stuctured and orchestrated.
Architectural patteers:
Its high Level and abstract
  - Are at module level
  - Address global concerns, such as security, performance, maintability etc
  by the way these software qualities are also called quality attributes
  unlike its cousin,
  # impact of design patterns
  the impact of design pattern is Local. 
  example singelton - focus on number of instances for same class.
  # Impact on Architectural patterns:
  Global, direct impact on overall quality of your software
  example MVC, in this quality attributes is maintability
  by decoupling the resposibilities of a typical by replication
  into three distinct modules. and limiting changes only to 
  unaffected modules. MVC improves software modifiability.
  for eg: if user interface needs to be changed programmers
  don't have to touch models and controller module

  # Patterns and Frameworks
  Design patterns are nice because they allow you to reuse the design solution
  however thay are not a trunkey solution you still have to write your own code
  That implements a patterns code samples are often available but it's necessary
  to customize them to fit your need.
  Good news:
  There are Exceptions - Domain specific software components.
  - commercial off-the-shelf(COTS) and open source frameworks
    in security.
  - There are many reusable snippets of code available 

# FrameWorks
refer to collection of reusable software components.
refer to collection of reusable software elements.
this frameworks implements design patterns
allows developer to reuse the code through application programing interfaces(APIS)
This means all you have to do as developer use them through their APIS
Scenario: Authentication
Several security Frameworks already offer user authetication Features
and support various programing Language. 
Spring Security, Bouncy Castel. Java authenticatin and authorization services or JAAS.
- Always look Frameworks before writing there own.

# Design pattern adoption
- mainstream use of design pattern are
- widely accepted and adopted by practitioners.
- indicators: Publication
- commercial off-the-shelf(COTS) and open source frameworks
    in security.
Quick search on amazon - software design patterns
Head First OOPS Analysis and design - book

# Approches to Organize Code
- Procedural programing: using functions
- OOPS - using properties and behaviours
procedural or object-oriented?
python is oops, more features using design patterns
Design pattern require OOPS.

# what make python OOP?
- class, attribute, method, constructor, Inheritance

# why use design pattern, or why not?
- Encourage fellow developers to adopt design patterns.
Selling Point is
- Time and Money
- developing well-crafted solution takes time and can rack up
  developments costs.
- Reuse - when reusing ready made design solutions.
- share code base. with your coworkers.

Important of shared Vocabulary
- Design pattern lingo - major contributor to software enginering vocabullary
- learning design pattern will make you better software engineer.





