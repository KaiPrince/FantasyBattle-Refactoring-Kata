from Damage import Damage
from Inventory import Inventory
from Stats import Stats
from Target import Target


class Player(Target):
    def __init__(self, inventory: Inventory, stats: Stats) -> None:
        self._stats = stats
        self._inventory = inventory

    def calculate_damage(self, other: Target) -> Damage:
        damage = Damage(0)

        damage = self._inventory.apply_damage(damage)
        damage = self._stats.apply_damage(damage)
        damage = other.apply_damage_soak(damage)

        return damage

    def get_soak(self, total_damage: int) -> int:
        # TODO: Not implemented yet
        #   Add friendly fire
        soak = total_damage
        return soak
