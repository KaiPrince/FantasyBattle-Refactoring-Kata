from Damage import Damage
from Inventory import Inventory
from Stats import Stats
from Target import Target


class Player(Target):
    def __init__(self, inventory: Inventory, stats: Stats) -> None:
        self._stats = stats
        self._inventory = inventory

    def calculate_damage(self) -> Damage:
        damage = Damage(0, basis="damage")
        damage = self._inventory.apply_damage(damage)
        damage = self._stats.apply_damage(damage)
        return damage

    def calculate_soak(self) -> Damage:
        # TODO: Not implemented yet
        #   Add friendly fire
        soak = Damage(0, basis="soak")

        return soak
