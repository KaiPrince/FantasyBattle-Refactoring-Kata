"""
* Project Name: FantasyBattle-Refactoring-Kata
* File Name: Soak.py
* Programmer: Kai Prince
* Date: Sat, Mar 25, 2023
* Description: This file contains a model for damage absorbtion.
"""


class Soak:
    amount: int

    def __init__(self, amount: int):
        self.amount = amount
