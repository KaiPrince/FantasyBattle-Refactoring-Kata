from Item import Item
from Damage import Damage


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

    def update_damage(self, damage: Damage) -> Damage:
        result = damage
        for item in [
            self._left_hand,
            self._right_hand,
            self._head,
            self._chest,
            self._feet,
        ]:
            result = item.update_damage(result)
        return result

    def update_soak(self, damage: Damage) -> Damage:
        # Future: implement damage soak by converting head, chest, and
        #   feet to Armor
        return damage
