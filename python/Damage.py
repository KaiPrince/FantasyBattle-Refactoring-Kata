class Damage:
    _amount: int
    _modifier: float
    _soak: int
    _soak_modifier: float

    def __init__(
        self,
        amount: int,
        modifier: float = 0.0,
        soak: int = 0,
        soak_modifier: float = 0.0,
    ) -> None:
        self._amount = amount
        self._modifier = modifier
        self._soak = soak
        self._soak_modifier = soak_modifier

    def add_damage(self, amount: int):
        total_amount = self._amount + amount
        return Damage(
            total_amount,
            self._modifier,
            self._soak,
            self._soak_modifier,
        )

    def add_damage_modifier(self, modifier: float):
        total_modifier = self._modifier + modifier
        return Damage(
            self._amount,
            total_modifier,
            self._soak,
            self._soak_modifier,
        )

    def add_soak(self, amount: int):
        total_soak = self._soak + amount
        return Damage(
            self._amount,
            self._modifier,
            total_soak,
            self._soak_modifier,
        )

    def add_soak_modifier(self, modifier: float):
        total_soak_modifier = self._soak_modifier + modifier
        return Damage(
            self._amount,
            self._modifier,
            self._soak,
            total_soak_modifier,
        )

    def calculate_damage(self) -> int:
        total_damage = round(self._amount * self._modifier)
        soak = round(self._soak * (self._soak_modifier + 1))
        result = max(0, total_damage - soak)
        return result
