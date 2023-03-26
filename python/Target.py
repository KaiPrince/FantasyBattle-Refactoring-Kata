from typing import List

from Armor import Armor
from Buff import Buff
from Damage import Damage

from abc import ABC, abstractmethod


class Target(ABC):
    @abstractmethod
    def calculate_damage(self) -> Damage:
        pass

    @abstractmethod
    def calculate_soak(self, damage: Damage) -> Damage:
        pass


class SimpleEnemy(Target):
    _armor: Armor
    _buffs: List[Buff]

    def __init__(self, armor: Armor, buffs: List[Buff]) -> None:
        self._armor = armor
        self._buffs = buffs

    def calculate_damage(self) -> Damage:
        return Damage(0)

    def calculate_soak(self, damage: Damage) -> Damage:
        result = self._armor.update_soak(damage)
        for buff in self._buffs:
            result = buff.update_soak(result)

        return result
