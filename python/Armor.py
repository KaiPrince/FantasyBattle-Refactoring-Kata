class Armor:
    def get_damage_soak(self) -> int:
        pass


class SimpleArmor(Armor):
    def __init__(self, damage_soak: int):
        self._damage_soak = damage_soak

    def get_damage_soak(self) -> int:
        return self._damage_soak
