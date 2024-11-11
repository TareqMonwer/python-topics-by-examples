class Character:
    def attack(self):
        pass


class Warrior(Character):
    def attack(self):
        print("Warrior attacks with a sword!")


class Mage(Character):
    def attack(self):
        print("Mage attacks with a spell!")


# Inheritance works, but what if a character needs unique combinations of abilities?
