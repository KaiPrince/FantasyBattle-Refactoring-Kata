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
from Item import Item
from Stats import Stats
from Target import SimpleEnemy
from Armor import Armor
from Buff import Buff


def test_player_calculate_damage():
    # Arrange
    player = _build_player()

    # Act
    damage = player.calculate_damage()

    # Assert
    assert damage._amount == 10
    assert damage._modifier - 5.2 < 0.01


def test_enemy_apply_damage_soak():
    # Arrange
    enemy = _build_enemy()

    # Act
    soak = enemy.calculate_soak()

    # Assert
    assert soak._amount == 5
    assert soak._modifier - 3 < 0.01


def test_damage_calculation_strategy():
    # Arrange
    player = _build_player()
    enemy = _build_enemy()
    damage = player.calculate_damage()
    soak = enemy.calculate_soak()

    # Act
    result = damage.calculate() - soak.calculate_soak()
    # Assert
    assert result == 42


def _build_player():
    # right_hand = BaseItem("excalibur", 20, 1.5)
    right_hand = Item("flashy sword of danger", 10, 1.0)
    left_hand = Item("round shield", 0, 1.4)
    head = Item("helmet of swiftness", 0, 1.2)
    chest = Item("breastplate of steel", 0, 1.4)
    feet = Item("ten league boots", 0, 0.1)
    equipment = Equipment(left_hand, right_hand, head, chest, feet)
    inventory = Inventory(equipment)
    stats = Stats(1)
    player = Player(inventory, stats)
    return player


def _build_enemy():
    armor = Armor(5)
    buffs = [Buff(1.0, 1.0)]
    target = SimpleEnemy(armor, buffs)
    return target
