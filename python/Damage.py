class Damage:
    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def subtract(self, other):
        return Damage(max(0, self.amount - other.amount))
