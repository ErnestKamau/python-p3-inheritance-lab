#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        knowledge = []
        self.knowledge = knowledge
    
    def learn(self, str):
        self.str = str
        self.knowledge.append(str)