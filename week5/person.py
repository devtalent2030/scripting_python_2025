"""
This module is a class called person which will be utilized as an example of OOP
This class will have the following attributes:
- name: str
- age: int
- height: float
- weight: float

This class will also have the following methods:
- __init__: Initializes the person with name, age, height, and weight.
- __str__: Returns a string representation of the person.
- is_studying: Returns True if the person is studying
- get_name & set_name: Get and set the name of the person.
- get_age & set_age: Get and set the age of the person.
- get_height & set_height: Get and set the height of the person.
- get_weight & set_weight: Get and set the weight of the person.
"""

class Person:
    def __init__(self, name: str, age: int, height: float, weight: float, studying: bool):
        """
        Initializes a Person object.

        Args:
            name (str): Name of the person.
            age (int): Age of the person.
            height (float): Height of the person in centimeters.
            weight (float): Weight of the person in kilograms.
            studying (bool): Whether the person is currently studying.
        """
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.studying = studying

    def is_studying(self) -> bool:
        """
        Checks if the person is currently studying.

        Returns:
            bool: True if the person is studying, False otherwise.
        """
        return self.studying

    def get_name(self) -> str:
        """
        Returns the name of the person.
        
        Returns:
            str: Name of the person.
        """
        return self.name

    def set_name(self, name: str):
        """
        Sets the name of the person.
        
        Args:
            name (str): New name for the person.
        """
        self.name = name

    def get_age(self) -> int:
        """
        Returns the age of the person.
        
        Returns:
            int: Age of the person.
        """
        return self.age

    def set_age(self, age: int):
        """
        Sets the age of the person.
        
        Args:
            age (int): New age for the person.
        """
        self.age = age

    def get_height(self) -> float:
        """
        Returns the height of the person.
        
        Returns:
            float: Height of the person in centimeters.
        """
        return self.height

    def set_height(self, height: float):
        """
        Sets the height of the person.

        Args:
            height (float): New height for the person in centimeters.
        """
        self.height = height

    def get_weight(self) -> float:
        """
        Returns the weight of the person.

        Returns:
            float: Weight of the person in kilograms.
        """
        return self.weight

    def set_weight(self, weight: float):
        """
        Sets the weight of the person.

        Args:
            weight (float): New weight for the person in kilograms.
        """
        self.weight = weight
        
    def __str__(self):
        """
        Returns a string representation of the person.
        
        Returns:
            str: String representation of the person.
        """
        return f"Person(name={self.name}, age={self.age}, height={self.height}, weight={self.weight}, studying={self.studying})"