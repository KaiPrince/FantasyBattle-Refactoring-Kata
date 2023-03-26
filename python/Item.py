class Item:
    pass


class BaseItem(Item):
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
