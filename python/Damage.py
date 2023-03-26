from Target import Target


class Damage:
    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = max(0, amount)

    def applySoak(self, soak: int):
        total_damage = self.amount - soak
        return Damage(total_damage)

    @staticmethod
    def betweenTargets(attacker: Target, defender: Target):
        total_damage = attacker.calculate_damage()
        soak = defender.calculate_soak(total_damage)
        return Damage(total_damage).applySoak(soak)
