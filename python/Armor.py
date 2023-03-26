from Damage import Damage


class Armor:
    def __init__(self, damage_soak: int):
        self._damage_soak = damage_soak

    def apply_damage_soak(
        self,
        soak: Damage,
    ) -> Damage:
        result = soak.add_amount(self._damage_soak)
        return result
