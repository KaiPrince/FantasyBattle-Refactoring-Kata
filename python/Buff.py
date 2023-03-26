class Buff:
    pass


class BasicBuff(Buff):
    def __init__(self, soak_modifier: float, damage_modifier: float) -> None:
        self._soak_modifier = soak_modifier
        self._damage_modifier = damage_modifier
