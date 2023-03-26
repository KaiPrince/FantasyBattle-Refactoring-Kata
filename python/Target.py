from typing import List

from Armor import Armor
from Buff import Buff
from Damage import Damage


class Target:
    def apply_damage_soak(self, damage: Damage) -> Damage:
        pass


class SimpleEnemy(Target):
    _armor: Armor
    _buffs: List[Buff]

    def __init__(self, armor: Armor, buffs: List[Buff]) -> None:
        self._armor = armor
        self._buffs = buffs

    def apply_damage_soak(self, damage: Damage) -> Damage:
        result = self._armor.apply_damage_soak(damage)
        for buff in self._buffs:
            result = buff.apply_damage_soak(result)
        return result
