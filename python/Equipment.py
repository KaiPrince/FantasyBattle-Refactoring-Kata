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
        self.chest = chest
        self.feet = feet
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.head = head

    def get_damage(self):
        return self.left_hand.base_damage + self.right_hand.base_damage

    def get_damage_modifier(self):
        return self.left_hand.damage_modifier + self.right_hand.damage_modifier

    def get_soak(self):
        # TODO implement damage soak
        return 0
