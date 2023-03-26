from Equipment import Equipment
from Damage import Damage


class Inventory:
    def __init__(self, equipment: Equipment):
        self._equipment = equipment

    def apply_damage(self, damage: Damage) -> Damage:
        return self._equipment.apply_damage(damage)
