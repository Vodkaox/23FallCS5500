# Exercises

## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
    It's a concrete class. It has no abstract methods.

2. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
    It defines behavior for when an object is garbage collected.

3. What class does Texture inherit from?
    Image.

4. What methods and attributes does the Texture class inherit from 'Image'? 
    All the methods and attributes of the Image class

5. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
    It depends on the usage. If a Texture is an Image with some specialized properties, an 'is-a' relationship is better. However, if a Texture uses an image to represent itself, then a 'has-a' relationship would be better. 

    Code for 'has-a' relationship:
    class Texture(Image):
      def __init__(self, w, h):
        self.image = Image(w, h)

6. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
    Yes.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

2. Are singleton's in Python thread safe? Why or why not?
    No, if multiple threads try to create instances of a single instance class at the same time, there is a race condition that may result in multiple instances being created.
