from Damage import Damage


class Armor:
    def update_soak(damage: int) -> int:
        pass


class SimpleArmor(Armor):
    _damage_soak: int

    def __init__(self, damage_soak):
        self._damage_soak = damage_soak

    def update_soak(self, damage: Damage) -> Damage:
        return damage.apply_soak(self._damage_soak)
