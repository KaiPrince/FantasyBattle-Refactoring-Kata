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
    left_hand = BaseItem("left hand", 1, 1.0)
    right_hand = BaseItem("right hand", 1, 1.5)
    head = BaseItem("head", 1, 1.0)
    chest = BaseItem("chest", 1, 1.0)
    feet = BaseItem("feet", 1, 1.0)
    equipment = Equipment(left_hand, right_hand, head, chest, feet)
    inventory = Inventory()
    stats = Stats(1)
    player = Player(inventory, equipment, stats)

    # Act
    damage = player.calculate_damage()

    # Assert
    print(damage)
    assert damage == 28


def damage_between_targets_test():
    # Arrange
    left_hand = BaseItem("left hand", 1, 1.0)
    right_hand = BaseItem("right hand", 1, 1.5)
    head = BaseItem("head", 1, 1.0)
    chest = BaseItem("chest", 1, 1.0)
    feet = BaseItem("feet", 1, 1.0)
    equipment = Equipment(left_hand, right_hand, head, chest, feet)
    inventory = Inventory()
    stats = Stats(1)
    player = Player(inventory, equipment, stats)
    armor = SimpleArmor(1)
    buffs = [BasicBuff(1.0, 1.5)]
    target = SimpleEnemy(armor, buffs)

    # Act
    result = Damage.betweenTargets(player, target)

    # Assert
    print(result.amount)
    assert result.amount == 26


player_calculate_damage_test()
damage_between_targets_test()
