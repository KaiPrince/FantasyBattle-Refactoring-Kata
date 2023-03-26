from Item import Item


class Equipment:
    def __init__(
        self,
        left_hand: Item,
        right_hand: Item,
        head: Item,
        chest: Item,
        feet: Item,
    ) -> None:
        self._chest = chest
        self._feet = feet
        self._left_hand = left_hand
        self._right_hand = right_hand
        self._head = head

    def get_base_damage(self) -> int:
        return (
            self._left_hand.get_base_damage()
            + self._right_hand.get_base_damage()
            + self._head.get_base_damage()
            + self._feet.get_base_damage()
            + self._chest.get_base_damage()
        )

    def get_damage_modifier(self) -> float:
        return (
            self._left_hand.get_damage_modifier()
            + self._right_hand.get_damage_modifier()
            + self._head.get_damage_modifier()
            + self._feet.get_damage_modifier()
            + self._chest.get_damage_modifier()
        )
