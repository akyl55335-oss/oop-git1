from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(self.name, self.level)

    def rest(self):
        print(self.name)
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):
    def attack(self):
        print(self.name)


class Mage(Hero):
    def attack(self):
        print(self.name)


class Assassin(Hero):
    def attack(self):
        print(self.name)


warrior = Warrior("Артас", 5, 10, 8)
mage = Mage("Мерлин", 7, 12, 5)
assassin = Assassin("Эцио", 6, 9, 7)

for hero in (warrior, mage, assassin):
    hero.greet()
    hero.attack()
    hero.rest()
