# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Buatlah sebuah modul game
# Modul tersebut memiliki fungsi terkait Hero, Item, Enemy, Area dan Rank
# Lalu import modul game tersebut ke satu file python bernama main.py

from game import Hero, Item, Enemy, Area, Rank

# Contoh penggunaan modul game
player_hero = Hero("Sang Pahlawan", 100, 20)
enemy = Enemy("Monster", 50, 10)
sword = Item("Magic Sword", "A powerful sword with magical abilities")
forest_area = Area("Dark Forest", "A mysterious and dangerous forest")
hero_rank = Rank("Heroic", 5)

print(f"{player_hero.name} enters the {forest_area.name}.")
print(f"{player_hero.name} encounters a {enemy.name}.")

while enemy.health > 0:
  player_hero.attack(enemy)
  print(f"{enemy.name} health: {enemy.health}")

print(f"{enemy.name} already death.")

print(f"{player_hero.name} finds a {sword.name}: {sword.description}")

print(f"{player_hero.name} achieves the {hero_rank.name} rank at level {hero_rank.level}.")
