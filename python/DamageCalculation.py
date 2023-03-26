"""
* Project Name: FantasyBattle-Refactoring-Kata
* File Name: DamageCalculation.py
* Programmer: Kai Prince
* Date: Sat, Mar 25, 2023
* Description: This file contains a class for applying damage to targets.
"""
from Target import Target
from DamageValue import DamageValue


# I would have preferred to make this a method on Damage, but I hit a
#  circular import
class DamageCalculation:
    @staticmethod
    def betweenTargets(attacker: Target, defender: Target) -> DamageValue:
        total_damage = attacker.calculate_damage()
        soak = defender.calculate_soak(total_damage)
        return total_damage.applySoak(soak)
