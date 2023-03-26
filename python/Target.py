from typing import List

from Armor import Armor
from Buff import Buff


class Target:
    def is_player() -> bool:
        pass

    def is_simple_enemy() -> bool:
        pass

    def __get_soak_2(self, total_damage: int) -> int:
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

    def __get_soak_2(self, total_damage: int) -> int:
        if self.is_player():
            # TODO: Not implemented yet
            #   Add friendly fire
            soak = total_damage
        elif self.is_simple_enemy():
            soak = Player.__get_soak_for_simple_enemy(self)
        return soak
