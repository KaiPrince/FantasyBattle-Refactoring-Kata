from Equipment import Equipment


class Inventory:
    def __init__(self, equipment: Equipment):
        self._equipment = equipment

    def get_base_damage(self) -> int:
        return self._equipment.get_base_damage()

    def get_damage_modifier(self) -> float:
        return self._equipment.get_damage_modifier()
