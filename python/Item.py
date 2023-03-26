from Damage import Damage


class Item:
    name: str

    def __init__(
        self,
        name: str,
        base_damage: int,
        damage_modifier: float,
    ) -> None:
        self._name = name
        self._base_damage = base_damage
        self._damage_modifier = damage_modifier

    def apply_damage(self, damage: Damage) -> Damage:
        with_damage = damage.add_damage(self._base_damage)
        result = with_damage.add_damage_modifier(self._damage_modifier)
        return result
