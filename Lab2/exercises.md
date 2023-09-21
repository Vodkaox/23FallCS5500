# Exercises

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

Yes. If a function perform multiple actions or returns a value in addition to its main purpose, it is helpful to include that information in the function name.

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

A dictionary is an unordered collection of key-value pairs, where each key is unique and associated with a corresponding value.
A list is an ordered collection of items that can be of any data type.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

Yes.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

pros: flexibility; code reuse; generic algorithms. 
cons: performance; lack of specialization; increased complexity.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

Yes, the functions are well named.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

Yes, def create_user(name, age, email, address, phone, gender, username).

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

In Python, **kwargs is a special syntax that allows a method (or function) to receive an arbitrary number of keyword arguments as a dictionary. The term "kwargs" stands for "keyword arguments". The double asterisks (**) before "kwargs" indicate that the arguments will be collected into a dictionary.

Having a **kwargs argument in a method can be beneficial in several ways: flexibility; extensibility; pass-through. However, there are also cases where using **kwargs might have certain drawbacks: lack of type safety; potential ambiguity; overuse and complexity.

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

Why: The use of None as a default argument value in the methods of the Session class serves a specific purpose. By setting an argument to None, it allows the argument to be optional and provides a default behavior if the caller does not provide a specific value for that argument.

Why might it be good to set an argument by some predetermined value: By providing a default value, the method ensures that a specific behavior is maintained in cases where the caller does not provide an argument. This can improve code consistency and clarity. Default arguments simplify method invocations by allowing the caller to omit certain arguments when the default behavior is sufficient. This can make code more concise and readable. Users of the method have the flexibility to override the default behavior by explicitly providing a different value for the argument.
