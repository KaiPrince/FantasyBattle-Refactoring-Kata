from Equipment import Equipment
from Inventory import Inventory
from Stats import Stats
from Target import Target
from Damage import Damage


class Player(Target):
    def __init__(
        self,
        inventory: Inventory,
        equipment: Equipment,
        stats: Stats,
    ) -> None:
        self._stats = stats
        self._inventory = inventory
        self._equipment = equipment

    def calculate_damage(self) -> Damage:
        damage = Damage(0)
        damage = self._equipment.update_damage(damage)
        damage = self._stats.update_damage(damage)
        return damage

    def calculate_soak(self, damage: Damage) -> Damage:
        return self._equipment.update_soak(damage)
