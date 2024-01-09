# from typing import Self


# class Time:
#     def __init__(self, minutes, seconds):
#         self.minutes = minutes
#         self.seconds = seconds
    
#     def __add__(self, other:Self):
#         minutes = self.minutes + other.minutes
#         seconds = self.seconds + other.seconds
#         minutes += seconds // 60
#         seconds = seconds % 60
#         return Time(minutes,seconds)
    
#     def info(self):
#         return f"{self.minutes}:{self.seconds}"

# class Person:
#     total = 0
    
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         Person.total+=1
        
#     @staticmethod
#     def create_person(name, age, gender):
#         return Person(name, age, gender)
    
#     @classmethod
#     def count_total(cls):
#         return cls.total
    
    
    
    
# person_1 = Person("Yerkanat", 51, "Male")
# person = Person.create_person("Yerkanat", 51, "Male")
# print(Person.count_total())
from datetime import date

class Person:
    '''This class supposed to create Person object'''
    
    total = 0
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.total += 1

    @classmethod
    def count(cls):
        return cls.total
    
    @staticmethod
    def create_person(name, birth_year, gender):
        age = date.today().year - birth_year 
        return Person(name, age ,gender)
    
    def get_name(self):
        return self.name
    
    @property
    def get_age(self):
        return self.age



print(Person.count())