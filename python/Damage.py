class Damage:
    _amount: int
    _modifier: float
    _basis = "damage"

    def __init__(
        self,
        amount: int,
        modifier: float = 0.0,
        basis="damage",
    ) -> None:
        self._amount = amount
        self._modifier = modifier
        self._basis = basis

    def add_amount(self, amount: int):
        if self._basis == "damage":
            total_amount = self._amount + amount
            return Damage(
                total_amount,
                self._modifier,
                basis="damage",
            )
        else:
            total_soak = self._amount + amount
            return Damage(
                total_soak,
                self._modifier,
                basis="soak",
            )

    def add_modifier(self, modifier: float):
        if self._basis == "damage":
            total_modifier = self._modifier + modifier
            return Damage(
                self._amount,
                total_modifier,
                basis="damage",
            )
        else:
            total_modifier = self._modifier + modifier
            return Damage(
                self._amount,
                total_modifier,
                basis="soak",
            )

    def calculate(self) -> int:
        if self._basis == "damage":
            total_damage = round(self._amount * self._modifier)
            return total_damage
        else:
            total_damage = round(self._amount * (self._modifier + 1))
            return total_damage
