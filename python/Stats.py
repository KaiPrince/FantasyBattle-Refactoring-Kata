class Stats:
    def __init__(self, strength: int) -> None:
        self.strength = strength

    def get_damage_modifier(self):
        strength_modifier: float = self.strength * 0.1
        return strength_modifier
