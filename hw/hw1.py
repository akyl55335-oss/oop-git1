class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(self.name, self.level)

    def attack(self):
        print(self.name)
        self.strength -= 1

    def rest(self):
        print(self.name)
        self.health += 1


hero1 = Hero("Asuno", 5, 10, 7)
hero2 = Hero("Kirito", 3, 8, 5)

hero1.greet()
hero1.attack()
hero1.rest()
print(f"name={hero1.name}: lvl={hero1.level}, hp={hero1.health}, strength={hero1.strength}")

print(40)

hero2.greet()
hero2.attack()
hero2.rest()
print(f" name={hero2.name}: lvl={hero2.level}, hp={hero2.health}, strength={hero2.strength}")






