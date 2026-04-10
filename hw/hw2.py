import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(self.name,self.level)

    def attack(self):
        print(self.name)
        self.strength -= 1

    def rest(self):
        print(self.name)
        self.health += 1


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(self.name)


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(self.name)


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(self.name)


warrior = Warrior("Воин", 5, 100, 20, 50)
mage = Mage("Маг", 5, 80, 15, 100)
assassin = Assassin("Ассасин", 5, 90, 25, 70)

import random

heroes = ["Warrior", "Mage", "Assassin"]

def battle(player_choice, opponent_choice):
    print("Игрок выбрал:", player_choice)
    print("Противник выбрал:", opponent_choice)

    if player_choice == opponent_choice:
        print("Ничья!")
    elif (player_choice == "Warrior" and opponent_choice == "Assassin") or \
         (player_choice == "Assassin" and opponent_choice == "Mage") or \
         (player_choice == "Mage" and opponent_choice == "Warrior"):
        print("Победил:", player_choice)
    else:
        print("Победил:", opponent_choice)


# Запуск игры
player_choice = input("Выберите героя (Warrior / Mage / Assassin): ").capitalize()
if player_choice not in heroes:
    print("Неверный выбор!")
else:
    opponent_choice = random.choice(heroes)
    battle(player_choice, opponent_choice)




