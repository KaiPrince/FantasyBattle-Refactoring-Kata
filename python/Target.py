from typing import List

from Armor import Armor
from Buff import Buff


class Target:
    def is_player() -> bool:
        pass

    def is_simple_enemy() -> bool:
        pass


class SimpleEnemy(Target):
    armor: Armor
    buffs: List[Buff]

    def __init__(self, armor: Armor, buffs: List[Buff]) -> None:
        self.armor = armor
        self.buffs = buffs

    def is_player() -> bool:
        return False

    def is_simple_enemy() -> bool:
        return True
