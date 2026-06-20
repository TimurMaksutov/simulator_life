import random
from typing import List, Optional
from organism import Organism, Animal


class Ecosystem:

    def __init__(self) -> None:
        self.organisms: List[Organism] = []
        self.day = 0

    def add_organism(self, organism: Organism) -> None:
        self.organisms.append(organism)

    def remove_organism(self, organism: Organism) -> None:
        if organism in self.organisms:
            self.organisms.remove(organism)

    def find_prey(self, predator: Animal) -> Optional[Organism]:
        candidates = [org for org in self.organisms
                      if org is not predator and org.is_alive and isinstance(org, Animal)]
        if not candidates:
            return None
        return random.choice(candidates)

    def get_sunlight(self) -> float:
        return random.uniform(0.5, 1.5)

    def simulate_day(self) -> None:
        self.day += 1
        print(f"\n--- День {self.day} ---")

        for org in list(self.organisms):
            if org.is_alive:
                org.act(self)

        self.organisms = [org for org in self.organisms if org.is_alive]
        print(f"В экосистеме {len(self.organisms)} живых организмов.")

    def run(self, days: int) -> None:
        for _ in range(days):
            self.simulate_day()
            if not self.organisms:
                print("Все организмы вымерли.")
                break

    def __repr__(self) -> str:
        return f"Ecosystem(day={self.day}, organisms={len(self.organisms)})"