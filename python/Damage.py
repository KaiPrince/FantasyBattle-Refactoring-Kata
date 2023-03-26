from Target import Target


class Damage:
    amount: int

    def __init__(self, amount: int) -> None:
        self.amount = amount

    @staticmethod
    def onTarget(attacker: Target, defender: Target):
        total_damage = attacker.get_damage()
        soak = defender.get_soak(total_damage)
        return Damage(max(0, total_damage - soak))
