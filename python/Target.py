from typing import List

from Armor import Armor
from Buff import Buff

from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def calculate_damage(self) -> int:
        pass

    @abstractmethod
    def calculate_soak(self, damage: int) -> int:
        pass


class SimpleEnemy(Target):
    armor: Armor
    buffs: List[Buff]

    def __init__(self, armor: Armor, buffs: List[Buff]) -> None:
        self.armor = armor
        self.buffs = buffs

    def calculate_damage(self) -> int:
        return int(0)

    def calculate_soak(self, damage: int) -> int:
        amount = round(
            self.armor.damage_soak
            * (sum(buff.soak_modifier for buff in self.buffs) + 1)
        )
        return amount
