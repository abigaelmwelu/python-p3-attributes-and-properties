#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    pass
class Dog:
    def __init__(self):
        self._name = None
        self._breed = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        approved_breeds = ["French Bulldog","Chihuahua","Pointer" ]  # approved breeds
        if value in approved_breeds:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

# Create an instance of the Dog class
dog = Dog()

# Testing the properties
dog.name = "Buddy"  # Valid name
dog.breed = "Pug"  # Valid breed

dog.name = "This is a very long name that exceeds the limit"  # Invalid name
dog.breed = "Golden Retriever"  # Invalid breed

