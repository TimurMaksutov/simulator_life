from abc import ABC, abstractmethod
import random


class Organism(ABC):

    def __init__(self, name: str, energy: float) -> None:
        self.name = name
        self.energy = energy
        self.is_alive = True

    def eat(self, food_energy: float) -> None:
        if not self.is_alive:
            print(f"{self.name} мёртв и не может есть.")
            return
        self.energy += food_energy
        print(f"{self.name} съел и получил {food_energy:.1f} энергии.")

    def lose_energy(self, amount: float) -> None:
        if not self.is_alive:
            return
        self.energy -= amount
        if self.energy <= 0:
            self.energy = 0
            self.is_alive = False
            print(f"{self.name} погиб от истощения.")
        else:
            print(f"{self.name} потратил {amount:.1f} энергии, осталось {self.energy:.1f}.")

    @abstractmethod
    def act(self, ecosystem: 'Ecosystem') -> None:
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name}, energy={self.energy:.1f}, alive={self.is_alive})"


class Animal(Organism):

    def __init__(self, name: str, energy: float, speed: float = 1.0) -> None:
        super().__init__(name, energy)
        self.speed = speed

    def act(self, ecosystem: 'Ecosystem') -> None:
        if not self.is_alive:
            return

        self.lose_energy(5.0)
        if not self.is_alive:
            return

        prey = ecosystem.find_prey(self)
        if prey:
            success_prob = min(0.9, (self.energy / (self.energy + prey.energy)) * self.speed)
            if random.random() < success_prob:
                gained = prey.energy * 0.5
                self.eat(gained)
                ecosystem.remove_organism(prey)
                print(f"{self.name} съел {prey.name}.")
            else:
                print(f"{self.name} не смог поймать {prey.name}.")
        else:
            print(f"{self.name} не нашёл добычи.")


class Plant(Organism):

    def __init__(self, name: str, energy: float, growth_rate: float = 2.0) -> None:
        super().__init__(name, energy)
        self.growth_rate = growth_rate

    def act(self, ecosystem: 'Ecosystem') -> None:
        if not self.is_alive:
            return

        sunlight = ecosystem.get_sunlight()
        gained = self.growth_rate * sunlight
        self.eat(gained)

        self.lose_energy(2.0)
        if not self.is_alive:
            print(f"{self.name} засохло.")

        if self.energy > 30 and random.random() < 0.1:
            child = Plant(
                name=f"{self.name}_child_{id(self)}",
                energy=self.energy * 0.3,
                growth_rate=self.growth_rate
            )
            ecosystem.add_organism(child)
            self.energy *= 0.7
            print(f"{self.name} дало потомство: {child.name}.")