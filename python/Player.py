from Damage import Damage
from Inventory import Inventory
from Stats import Stats
from Target import Target


class Player(Target):
    def __init__(self, inventory: Inventory, stats: Stats) -> None:
        self._stats = stats
        self._inventory = inventory

    def calculate_damage(self, other: Target) -> Damage:
        base_damage = self._inventory.get_base_damage()
        damage_modifier = self.__get_damage_modifier()
        total_damage = round(base_damage * damage_modifier)
        soak = other.get_soak(total_damage)
        return Damage(max(0, total_damage - soak))

    def __get_damage_modifier(self):
        inventory_modifier = self._inventory.get_damage_modifier()
        stats_modifier = self._stats.get_damage_modifier()
        total_modifier = inventory_modifier + stats_modifier
        return total_modifier

    def get_soak(self, total_damage: int) -> int:
        # TODO: Not implemented yet
        #   Add friendly fire
        soak = total_damage
        return soak
