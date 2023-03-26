from Damage import Damage


class Stats:
    def __init__(self, strength: int) -> None:
        self._strength = strength

    def update_damage(self, damage: Damage) -> Damage:
        strength_modifier: float = self._strength * 0.1
        return damage.apply_damage(0, strength_modifier)
