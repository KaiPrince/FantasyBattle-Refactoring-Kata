from Damage import Damage
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

    def calculate_damage(self) -> Damage:
        base_damage = self.__get_base_damage()
        damage_modifier = self.__get_damage_modifier()
        total_damage = round(base_damage * damage_modifier)
        return Damage(total_damage)

    def __get_base_damage(self):
        return self.equipment.get_damage()

    def __get_damage_modifier(self):
        equipment_damage_modifier = self.equipment.get_damage_modifier()
        stats_damage_modifier = self.stats.get_damage_modifier()
        return stats_damage_modifier + equipment_damage_modifier

    def get_soak(self, damage: int):
        # TODO: Not implemented yet
        #   Add friendly fire
        soak: int = damage

        return soak
