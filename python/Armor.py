from Damage import Damage


class Armor:
    def apply_damage_soak(self, damage: Damage) -> Damage:
        pass


class SimpleArmor(Armor):
    def __init__(self, damage_soak: int):
        self._damage_soak = damage_soak

    def apply_damage_soak(self, damage: Damage) -> Damage:
        result = damage.add_soak(self._damage_soak)
        return result
