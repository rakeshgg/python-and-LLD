# Quality attributes and Design patterns
- Quality attribute: overall quality meet the expectations of end users.
  these quality attribute includes non-functional requirements. such as 
  performance, Security, Maintainbility 
  scenario:
  Imagine an operating system
  that provides you all the features in the word. its voice activated
  and works with numeros devices plugged into your computer. However the os
  is extremly vulnerable to security attacks would you buy such os if you have
  options. 
  OS Features are Functional Requirements
  - What the OS does.
  Security Properties
  Non-functional requiremnts - what the os is

  - Design pattern are related to both functional and nonfunctional requiremnts
    They are tied to functional requiremnets beacuse they are design solution
    that enable a specific software features behing the scenes. for eg
    you can leverage the adpater patterns

    application - Adapter(Oracle Driver, MySQL driver) - Oracle DB, MySql DB
    handle your need to connect various dbs that neccesiate the use of it
    if adpater pattern Fails your software no longer Functions because it cannot
    communicate with its remote database anymore.
    If cosistently used, adpater pattern promotes maintainbility

# Design patterns
- More directly connected to functional requiremnts.
- Indirectly affect the quality attributes.

# domain specifc patterns
  many design pattern are of general purpose.
  domain specific design pattern 
  Domain: Context - In which set of design patterns are particularly relevent and useful.
  Examples of domain includes Real Time(RT), Human computer Interface(HCI), J2EE patterns, Security etc

  areas of application such as RT and HCI
  other are on tools and platforms 
  as core j2EE - platform
  Security - quality attribute

  # Domain-Neautral Patterns
  - Intentiinally left abstarct to maximize its coverage
  - Require Further Refinments in order to applied to solve a concrete problems

  # Advatage: Domain Specifc patterns
  Ease of adoption - already customized and optimized
  Example: security patterns
  - Encryption
  - Authentication
  - Input Validation

# security patterns
- Security knowlege is essensial, software more resilinace to this attack.
- many security patterns are available for you to check out and adopt in 
  your code.
- make software less vulernable to attack 
- confidential 
- can help software resist attcks - Encryption - Framework cryptography
- pip install cryptography
- Authenticate
- Authorize
- control access
- Maintain Integrity
- Limit Exposures
- Detect attack
- Recover from attacks
- securiy pattern also facilates acts of detecting attcks or recovering from attcks

# case study: Intercepting validators
input -> processing -> output
Hacking techiques on input
- Sql Injection
- cross site scripting (XSS)
to prevent - Input validation, user input contains any susspicious keyword
Sql injection leverges additional database commands.
Intercepting Validator - it intercept user input first before validating the content
bases on explanation so far you can see how domain specif pattern can naturally
emerges out of necessaity.
consistency is key. consitence through out the code base.
best way to use security pattern is to use same line of code in the form of Library
so that programmers can simply include them into their code whenever necessary.

# Intercepting validator Example
when yiu think about its concept is very similar to that of checkpoint
Learning more details about this pattern will boost your confidence
even more

client -->(Invokes) --> SecurebaseActions ---> Invokes(Target)
                            |(Validate parameters)
                            |
                        Intercepting/Validator --->(Creates)(Validate) Validator

SecurebaseActions - design pattern of its own right, direct intercat with client
 - Includes Authentication
 - Authorization
 - Input Validation
 - Logging
This pattern take advatage of command pattern to invoke the security methods
Intercepting/Validator - class is responsible for creating specialized validator objects
                         sequal validators
                         - paramter validator
                         - SQL Validator
    when client make request for resource Intercepting/Validator get in the middle
    and send the request to appropriate validators. in our example the validator
    look for any malformed parameters and sql keywords once inception process is
    over. a SecurebaseActions objects allow the client to have acess to the 
    request resouce.
By creating the overall Infrastucture to handle user inputs and make it availabe
to all the developers involved in your project. you can avoid duplicate efforts
and make a strong case for adopting intervalidation whenever necessary. your team
member have no excuse. because secure code is reusing the same code base




