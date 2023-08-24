#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    pass
class Person:
    approved_jobs = ["Marketing", "Sales", "Finance"]  # approved jobs

    def __init__(self):
        self._name = None
        self._job = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) < 25:
            self._name = value.title()
        else:
            print("Name must be a string under 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in self.approved_jobs:
            self._job = value
        else:
            print("The job must be in the following list of jobs")

# Create an instance of the Person class
person = Person()

# Testing the properties
person.name = "john"  # Valid name
person.job = "Customer Service"  # Valid job

person.name = "this is a very long name that exceeds the limit"  # Invalid name
person.job = "Writer"  # Invalid job


