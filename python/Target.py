from typing import List

from Armor import Armor
from Buff import Buff


class Target:
    def get_soak(self, total_damage: int) -> int:
        pass


class SimpleEnemy(Target):
    _armor: Armor
    _buffs: List[Buff]

    def __init__(self, armor: Armor, buffs: List[Buff]) -> None:
        self._armor = armor
        self._buffs = buffs

    def get_soak(self, total_damage: int) -> int:
        soak = round(
            self._armor.damage_soak
            * (sum(buff.soak_modifier for buff in self._buffs) + 1)
        )
        return soak
