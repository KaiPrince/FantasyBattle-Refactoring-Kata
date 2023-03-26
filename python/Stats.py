class Stats:
    def __init__(self, strength: int) -> None:
        self._strength = strength

    def get_damage_modifier(self) -> float:
        strength_modifier: float = self._strength * 0.1
        return strength_modifier
