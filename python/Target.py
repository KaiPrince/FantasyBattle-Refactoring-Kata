from typing import List

from Armor import Armor
from Buff import Buff
from Damage import Damage
from DamageCalculationStrategy import SoakCalculationStrategy


class Target:
    def calculate_soak(self) -> Damage:
        pass


class SimpleEnemy(Target):
    _armor: Armor
    _buffs: List[Buff]

    def __init__(self, armor: Armor, buffs: List[Buff]) -> None:
        self._armor = armor
        self._buffs = buffs

    def calculate_soak(self) -> Damage:
        soak = Damage(SoakCalculationStrategy(), 0)
        soak = self._armor.apply_damage_soak(soak)
        for buff in self._buffs:
            soak = buff.apply_damage_soak(soak)
        return soak
