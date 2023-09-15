"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # Getter methods
    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    # Setter methods
    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    @abstractmethod
    def set_values(self, width, height):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def set_values(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def area(self):
        return self.get_width() * self.get_height()


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle(3, 4)

    # Call a member function
    print("area:", rect.area())

    # Use setter methods to change values
    rect.set_width(5)
    rect.set_height(6)
    print("new_area:", rect.area())

    # Use getter methods to retrieve values
    print("Width:", rect.get_width())
    print("Height:", rect.get_height())
