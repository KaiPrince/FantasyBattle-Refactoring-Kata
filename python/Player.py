from Damage import Damage
from Equipment import Equipment
from Inventory import Inventory
from Item import Item
from Stats import Stats
from Target import Target, SimpleEnemy


class Player(Target):
    def __init__(self, inventory: Inventory, stats: Stats) -> None:
        self.stats = stats
        self.inventory = inventory

    def calculate_damage(self, other: Target) -> Damage:
        base_damage = self.__get_base_damage()
        damage_modifier = self.__get_damage_modifier()
        total_damage = round(base_damage * damage_modifier)
        soak = self.__get_soak(other, total_damage)
        return Damage(max(0, total_damage - soak))

    def __get_base_damage(self):
        inventory: Inventory = self.inventory
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
        equipment: Equipment = self.inventory.equipment
        return self.__do_damage_modifier_calculation(
            equipment.left_hand,
            equipment.right_hand,
            equipment.head,
            equipment.feet,
            equipment.chest,
            self.stats,
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
        strength_modifier: float = stats.strength * 0.1
        return (
            strength_modifier
            + left_hand.damage_modifier
            + right_hand.damage_modifier
            + head.damage_modifier
            + feet.damage_modifier
            + chest.damage_modifier
        )

    @staticmethod
    def __get_soak(other: Target, total_damage: int):
        soak: int = Player.__do_get_soak(other, total_damage)
        return soak

    @staticmethod
    def __do_get_soak(other: Target, total_damage: int) -> int:
        if other.is_player():
            # TODO: Not implemented yet
            #   Add friendly fire
            soak = total_damage
        elif other.is_simple_enemy():
            soak = Player.__get_soak_for_simple_enemy(other)
        return soak

    @staticmethod
    def __get_soak_for_simple_enemy(simple_enemy: SimpleEnemy):
        soak = round(
            simple_enemy.armor.damage_soak
            * (sum(buff.soak_modifier for buff in simple_enemy.buffs) + 1)
        )

        return soak

    def is_player() -> bool:
        return True

    def is_simple_enemy() -> bool:
        return False
