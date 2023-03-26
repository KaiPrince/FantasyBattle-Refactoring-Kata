from Damage import Damage


class Stats:
    def __init__(self, strength: int) -> None:
        self._strength = strength

    def apply_damage(self, damage: Damage) -> Damage:
        strength_modifier: float = self._strength * 0.1
        result = damage.add_modifier(strength_modifier)
        return result
