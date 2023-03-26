from Soak import Soak


class Armor:
    def __init__(self, damage_soak: int):
        self._damage_soak = damage_soak

    def apply_damage_soak(
        self,
        soak: Soak,
    ) -> Soak:
        result = soak.add_amount(self._damage_soak)
        return result
