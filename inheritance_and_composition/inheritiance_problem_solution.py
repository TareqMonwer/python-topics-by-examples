class AttackBehavior:
    def attack(self):
        print("Attacking...")


class DefenseBehavior:
    def defend(self):
        print("Defending...")


class HealerBehavior:
    def heal(self):
        print("Healing...")


class Character:
    def __init__(
        self, attack_behavior, defense_behavior, healer_behavior=None
    ):
        self.attack_behavior = attack_behavior
        self.defense_behavior = defense_behavior
        self.healer_behavior = healer_behavior

    def attack(self):
        self.attack_behavior.attack()

    def defend(self):
        self.defense_behavior.defend()

    def heal(self):
        if self.healer_behavior:
            self.healer_behavior.heal()


# Flexible character creation
warrior = Character(AttackBehavior(), DefenseBehavior())
mage = Character(AttackBehavior(), DefenseBehavior(), HealerBehavior())

warrior.attack()  # Output: Attacking...
mage.heal()  # Output: Healing...
