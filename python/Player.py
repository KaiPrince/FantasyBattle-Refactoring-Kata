from Damage import Damage
from Equipment import Equipment
from Inventory import Inventory
from Item import Item
from Stats import Stats
from Target import Target


class Player(Target):
    def __init__(self, inventory: Inventory, stats: Stats) -> None:
        self._stats = stats
        self._inventory = inventory

    def calculate_damage(self, other: Target) -> Damage:
        base_damage = self.__get_base_damage()
        damage_modifier = self.__get_damage_modifier()
        total_damage = round(base_damage * damage_modifier)
        soak = other.get_soak(total_damage)
        return Damage(max(0, total_damage - soak))

    def __get_base_damage(self):
        inventory: Inventory = self._inventory
        equipment: Equipment = inventory.equipment
        return self.__do_base_damage_calculation(
            equipment.left_hand,
            equipment.right_hand,
            equipment.head,
            equipment.feet,
            equipment.chest,
        )

    def __do_base_damage_calculation(
        self,
        left_hand: Item,
        right_hand: Item,
        head: Item,
        feet: Item,
        chest: Item,
    ):
        return (
            left_hand.base_damage
            + right_hand.base_damage
            + head.base_damage
            + feet.base_damage
            + chest.base_damage
        )

    def __get_damage_modifier(self):
        equipment: Equipment = self._inventory.equipment
        return self.__do_damage_modifier_calculation(
            equipment.left_hand,
            equipment.right_hand,
            equipment.head,
            equipment.feet,
            equipment.chest,
            self._stats,
        )

    def __do_damage_modifier_calculation(
        self,
        left_hand: Item,
        right_hand: Item,
        head: Item,
        feet: Item,
        chest: Item,
        stats: Stats,
    ):
        strength_modifier: float = stats._strength * 0.1
        return (
            strength_modifier
            + left_hand.damage_modifier
            + right_hand.damage_modifier
            + head.damage_modifier
            + feet.damage_modifier
            + chest.damage_modifier
        )

    def get_soak(self, total_damage: int) -> int:
        # TODO: Not implemented yet
        #   Add friendly fire
        soak = total_damage
        return soak
