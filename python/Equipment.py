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
