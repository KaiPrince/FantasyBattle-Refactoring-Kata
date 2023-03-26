class Damage:
    _amount: int

    def __init__(self, amount: int) -> None:
        self._amount = amount

    def get_amount(self) -> int:
        return self._amount
