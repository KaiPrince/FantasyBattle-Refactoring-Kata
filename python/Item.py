class Item:
    def get_base_damage(self) -> int:
        pass

    def get_damage_modifier(self) -> float:
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

    def get_base_damage(self) -> int:
        return self._base_damage

    def get_damage_modifier(self) -> float:
        return self._damage_modifier
