#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method to calculate the area"""
        return self.__width * self.__height

    def display(self):
        """Public method to display the rectangle"""
        for i in range(self.__y):
            print("")
        for h in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """string magic method"""
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "
            f"- {self.__width}/{self.__height}."
        )

    def update(self, *args):
        """Public method: assigns an argument to each attribute"""
        i = 0
        for arg in args:
            if i == 0:
                self.id = arg
            if i == 1:
                self.__width = arg
            if i == 2:
                self.__height = arg
            if i == 3:
                self.__x = arg
            if i == 4:
                self.__y = arg
            i += 1
