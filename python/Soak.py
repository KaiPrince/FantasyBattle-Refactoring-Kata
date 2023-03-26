class Soak:
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
        total_soak = self._amount + amount
        return Soak(
            total_soak,
            self._modifier,
        )

    def add_modifier(self, modifier: float):
        total_modifier = self._modifier + modifier
        return Soak(
            self._amount,
            total_modifier,
        )

    def calculate_soak(self) -> int:
        total_damage = round(self._amount * (self._modifier + 1))
        return total_damage
