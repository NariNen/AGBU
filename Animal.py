class Animal:
    type = None
    name = None

    def eat(self, food):
        print(f"Animal is eating {food}")

    def sound(self, voice):
        print(f"Animal is make a sound {voice}")

    def legs(self,foot):
        print(f"Animal  have {foot} legs")
    def gender(self):
        print(f"{self.name} is of unknown gender")


# Example usage
superAnimal = Animal()

superAnimal.eat("meat")
superAnimal.sound("roar")
superAnimal.legs(4)
superAnimal.gender()

class Pet(Animal):




