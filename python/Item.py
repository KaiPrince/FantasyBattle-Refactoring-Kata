from Damage import Damage


class Item:
    def update_damage(self, damage: Damage) -> Damage:
        pass


class BaseItem(Item):
    name: str
    _base_damage: int
    _damage_modifier: float

    def __init__(
        self,
        name: str,
        base_damage: int,
        damage_modifier: float,
    ) -> None:
        self.name = name
        self._base_damage = base_damage
        self._damage_modifier = damage_modifier

    def update_damage(self, damage: Damage) -> Damage:
        return damage.apply_damage(self._base_damage, self._damage_modifier)
