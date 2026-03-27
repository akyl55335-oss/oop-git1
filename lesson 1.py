class hero:


    def __init__(self, name, hp, lvl):
        self.name_hero = name
        self.hp_hero = hp
        self.lvl_hero = lvl


kirito = hero('Kirito', 1000, 100)
Asuno = hero('Asuno', 1000, 100)

print(kirito.name_hero)
print(Asuno.hp_hero)
