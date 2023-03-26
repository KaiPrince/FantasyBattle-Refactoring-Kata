from Damage import Damage
from Soak import Soak


class Buff:
    def __init__(self, soak_modifier: float, damage_modifier: float) -> None:
        self._soak_modifier = soak_modifier
        self._damage_modifier = damage_modifier

    def apply_damage(self, damage: Damage) -> Damage:
        result = damage.add_modifier(self._damage_modifier)
        return result

    def apply_damage_soak(self, soak: Soak) -> Soak:
        result = soak.add_modifier(self._soak_modifier)
        return result
