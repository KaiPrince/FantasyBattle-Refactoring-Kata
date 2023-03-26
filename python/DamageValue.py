from Soak import Soak


class DamageValue:
    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = max(0, amount)

    def applySoak(self, other: Soak):
        total_damage = self.amount - other.amount
        return DamageValue(total_damage)
