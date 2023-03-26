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
        self._amount = max(0, amount)
        self._modifier = modifier
        self._soak = max(0, soak)
        self._soak_modifier = soak_modifier

    def apply_damage(self, damage: int, modifier: float = 0.0):
        total_damage = self._amount + damage
        total_modifier = self._modifier + modifier

        return Damage(
            total_damage,
            total_modifier,
            self._soak,
            self._soak_modifier,
        )

    def apply_soak(self, soak: int, modifier: float = 0.0):
        total_soak = self._soak + soak
        total_soak_modifier = self._soak_modifier + modifier
        return Damage(
            self._amount,
            self._modifier,
            total_soak,
            total_soak_modifier,
        )

    def calculate_damage(self) -> int:
        base_damage = self._amount * self._modifier
        soak = self._soak * self._soak_modifier
        return round(base_damage - soak)

    @staticmethod
    def betweenTargets(attacker, defender):  # Target, Target
        base_damage = attacker.calculate_damage()
        total_damage = defender.calculate_soak(base_damage)
        return total_damage
