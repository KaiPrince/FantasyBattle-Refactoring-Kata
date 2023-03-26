class Damage:
    _amount: int
    _modifier: float

    def __init__(
        self,
        amount: int,
        modifier: float = 0.0,
    ) -> None:
        self._amount = amount
        self._modifier = modifier

    def add_amount(self, amount: int):
        total_amount = self._amount + amount
        return Damage(
            total_amount,
            self._modifier,
        )

    def add_modifier(self, modifier: float):
        total_modifier = self._modifier + modifier
        return Damage(
            self._amount,
            total_modifier,
        )

    def calculate(self) -> int:
        total_damage = round(self._amount * self._modifier)
        return total_damage
