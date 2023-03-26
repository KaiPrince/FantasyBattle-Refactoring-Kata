class Buff:
    def get_soak_modifier(self) -> float:
        pass

    def get_damage_modifer(self) -> float:
        pass


class BasicBuff(Buff):
    def __init__(self, soak_modifier: float, damage_modifier: float) -> None:
        self._soak_modifier = soak_modifier
        self._damage_modifier = damage_modifier

    def get_soak_modifier(self) -> float:
        return self._soak_modifier

    def get_damage_modifer(self) -> float:
        return self._damage_modifier
