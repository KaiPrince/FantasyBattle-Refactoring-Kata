class CalculationStrategy:
    def calculate(self, base: int, modifier: float) -> int:
        pass


class DamageCalculationStrategy(CalculationStrategy):
    def calculate(
        self,
        base: int,
        modifier: float,
    ) -> int:
        total = round(base * modifier)
        return total


class SoakCalculationStrategy(CalculationStrategy):
    def calculate(
        self,
        base: int,
        modifier: float,
    ) -> int:
        total = round(base * (modifier + 1))
        return total
