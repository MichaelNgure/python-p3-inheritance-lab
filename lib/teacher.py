#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name):
    # Call super() / parent constructor
        super().__init__(first_name, last_name)
    # initialize knowledge
        self.knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]
    def teach(self):
        if len(self.knowledge) > 0:
            randomIndex = random.randint(0, len(self.knowledge))
            randomElement = self.knowledge[randomIndex]
            return randomElement