from DamageCalculationStrategy import CalculationStrategy


class Damage:
    _amount: int
    _modifier: float
    _strategy: CalculationStrategy

    def __init__(
        self,
        strategy: CalculationStrategy,
        amount: int,
        modifier: float = 0.0,
    ) -> None:
        self._strategy = strategy
        self._amount = amount
        self._modifier = modifier

    def add_amount(self, amount: int):
        total_amount = self._amount + amount
        return Damage(
            self._strategy,
            total_amount,
            self._modifier,
        )

    def add_modifier(self, modifier: float):
        total_modifier = self._modifier + modifier
        return Damage(
            self._strategy,
            self._amount,
            total_modifier,
        )

    def calculate(self) -> int:
        return self._strategy.calculate(self._amount, self._modifier)
