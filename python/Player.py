from Equipment import Equipment
from Inventory import Inventory
from Stats import Stats
from Target import Target


class Player(Target):
    def __init__(
        self,
        inventory: Inventory,
        equipment: Equipment,
        stats: Stats,
    ) -> None:
        self.stats = stats
        self.inventory = inventory
        self.equipment = equipment

    def calculate_damage(self) -> int:
        base_damage = self.equipment.get_damage()
        damage_modifier = self.__get_damage_modifier()
        total_damage = round(base_damage * damage_modifier)
        return total_damage

    def __get_damage_modifier(self):
        equipment_damage_modifier = self.equipment.get_damage_modifier()
        stats_damage_modifier = self.stats.get_damage_modifier()
        return stats_damage_modifier + equipment_damage_modifier

    def calculate_soak(self, damage: int) -> int:
        # TODO: Not implemented yet
        #   Add friendly fire
        amount: int = damage

        return amount
