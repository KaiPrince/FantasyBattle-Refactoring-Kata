from Damage import Damage


class Buff:
    def update_damage(damage: Damage) -> Damage:
        pass

    def update_soak(damage: Damage) -> Damage:
        pass


class BasicBuff(Buff):
    _soak_modifier: float
    _damage_modifier: float

    def __init__(self, soak_modifier: float, damage_modifier: float) -> None:
        self._soak_modifier = soak_modifier
        self._damage_modifier = damage_modifier

    def update_damage(self, damage: Damage) -> Damage:
        return damage.apply_damage(0, self._damage_modifier)

    def update_soak(self, damage: Damage) -> Damage:
        return damage.apply_soak(0, self._soak_modifier + 1)
