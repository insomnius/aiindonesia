class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        enemy.receive_damage(self.attack_power)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def receive_damage(self, damage):
        self.health -= damage

class Area:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Rank:
    def __init__(self, name, level):
        self.name = name
        self.level = level
