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
from Target import SimpleEnemy
from Armor import SimpleArmor
from Buff import BasicBuff


def test_player_calculate_damage():
    # Arrange
    player = _build_player()
    enemy = _build_enemy()

    # Act
    damage = player.calculate_damage(enemy)

    # Assert
    assert damage._amount == 42


def _build_player():
    # right_hand = BaseItem("excalibur", 20, 1.5)
    right_hand = BaseItem("flashy sword of danger", 10, 1.0)
    left_hand = BaseItem("round shield", 0, 1.4)
    head = BaseItem("helmet of swiftness", 0, 1.2)
    chest = BaseItem("breastplate of steel", 0, 1.4)
    feet = BaseItem("ten league boots", 0, 0.1)
    equipment = Equipment(left_hand, right_hand, head, chest, feet)
    inventory = Inventory(equipment)
    stats = Stats(1)
    player = Player(inventory, stats)
    return player


def _build_enemy():
    armor = SimpleArmor(5)
    buffs = [BasicBuff(1.0, 1.0)]
    target = SimpleEnemy(armor, buffs)
    return target
