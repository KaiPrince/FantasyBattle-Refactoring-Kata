class Armor:
    pass


class SimpleArmor(Armor):
    def __init__(self, damage_soak: int):
        self._damage_soak = damage_soak
