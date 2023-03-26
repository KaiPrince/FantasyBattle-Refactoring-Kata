"""
* Project Name: FantasyBattle-Refactoring-Kata
* File Name: player-test.py
* Programmer: Kai Prince
* Date: Sat, Mar 25, 2023
* Description: This file contains a unit test for the Player class.
"""
from Player import Player
from Inventory import Inventory
from Equipment import Equipment
from Item import BaseItem
from Stats import Stats
from Damage import Damage
from Target import SimpleEnemy
from Armor import SimpleArmor
from Buff import BasicBuff


def player_calculate_damage_test():
    # Arrange
    player = _build_player()

    # Act
    damage = player.calculate_damage()

    # Assert
    print(damage.calculate_damage())
    assert damage.calculate_damage() == 52


def damage_between_targets_test():
    # Arrange
    player = _build_player()
    enemy = _build_enemy()

    # Act
    result = Damage.betweenTargets(player, enemy)

    # Assert
    print(result.calculate_damage())
    assert result.calculate_damage() == 42


def damage_to_player_test():
    # Arrange
    player = _build_player()
    enemy = _build_enemy()

    # Act
    result = Damage.betweenTargets(enemy, player)

    # Assert
    print(result._amount)
    assert result._amount == 0


def _build_player():
    # right_hand = BaseItem("excalibur", 20, 1.5)
    right_hand = BaseItem("flashy sword of danger", 10, 1.0)
    left_hand = BaseItem("round shield", 0, 1.4)
    head = BaseItem("helmet of swiftness", 0, 1.2)
    chest = BaseItem("breastplate of steel", 0, 1.4)
    feet = BaseItem("ten league boots", 0, 0.1)
    equipment = Equipment(left_hand, right_hand, head, chest, feet)
    inventory = Inventory()
    stats = Stats(1)
    player = Player(inventory, equipment, stats)
    return player


def _build_enemy():
    armor = SimpleArmor(5)
    buffs = [BasicBuff(1.0, 1.0)]
    target = SimpleEnemy(armor, buffs)
    return target


player_calculate_damage_test()
damage_between_targets_test()
damage_to_player_test()
