# Copyright © 2022 Indonesia AI. All Rights Reserved.
# contact@aiforindonesia.org

# Kembangkanlah modul game yang sudah dibuat sebelumnya menjadi package
# Package tersebut berupa folder yang memuat modul-modul terkait Hero, Item, Enemy, Area dan Rank
# Lalu import package game tersebut ke satu file python bernama main.py

from game_package import hero, area, enemy, item, rank

# Contoh penggunaan modul game
player_hero = hero.Object("Sang Pahlawan", 100, 20)
enemy = enemy.Object("Monster", 50, 10)
sword = item.Object("Magic Sword", "A powerful sword with magical abilities")
forest_area = area.Object("Dark Forest", "A mysterious and dangerous forest")
hero_rank = rank.Object("Heroic", 5)

print(f"{player_hero.name} enters the {forest_area.name}.")
print(f"{player_hero.name} encounters a {enemy.name}.")

while enemy.health > 0:
  player_hero.attack(enemy)
  print(f"{enemy.name} health: {enemy.health}")

print(f"{enemy.name} already death.")

print(f"{player_hero.name} finds a {sword.name}: {sword.description}")

print(f"{player_hero.name} achieves the {hero_rank.name} rank at level {hero_rank.level}.")
