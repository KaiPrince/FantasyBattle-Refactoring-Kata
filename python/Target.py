from typing import List

from Armor import Armor
from Buff import Buff
from Damage import Damage
from Soak import Soak

from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def calculate_damage(self) -> Damage:
        pass

    @abstractmethod
    def calculate_soak(self, damage: Damage) -> Soak:
        pass


class SimpleEnemy(Target):
    armor: Armor
    buffs: List[Buff]

    def __init__(self, armor: Armor, buffs: List[Buff]) -> None:
        self.armor = armor
        self.buffs = buffs

    def calculate_damage(self) -> Damage:
        return Damage(0)

    def calculate_soak(self, damage: Damage) -> Soak:
        amount = round(
            self.armor.damage_soak
            * (sum(buff.soak_modifier for buff in self.buffs) + 1)
        )
        return Soak(amount)
