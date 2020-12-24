

from abc import ABC, abstractmethod


class Human(ABC):
    name=None
    position=0
    feed=0

    def __init__(self, name):
        self.name=name


    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def go(self):
        pass


class Doctor(Human):
    def go(self):
        self.position=self.position+4
        self.feed = self.feed - 3

    def eat(self):
        self.feed=self.feed+2


class Student(Human):
    def go(self):
        self.position = self.position + 4
        self.feed = self.feed - 5

    def eat(self):
        self.feed = self.feed + 6


class Sportsman(Human):
    def go(self):
        self.position = self.position + 8
        self.feed = self.feed - 6

    def eat(self):
        self.feed = self.feed + 7