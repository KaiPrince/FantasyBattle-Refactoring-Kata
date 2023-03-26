from Soak import Soak


class Damage:
    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def applySoak(self, other: Soak):
        total_damage = self.amount - other.amount
        return Damage(max(0, total_damage))
