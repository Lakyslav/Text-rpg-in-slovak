import random

class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def is_alive(self):  # Funkcia pre kontrolu života
        return self.hp > 0

    def attack(self):
        return random.randint(0, self.damage)

    def take_damage(self, damage):  # Pridanie metódy take_damage pre nepriateľa
        self.hp -= damage
        if self.hp <= 0:
            print(f"\033[32mHurá!, {self.name} bol porazený!\033[0m")
