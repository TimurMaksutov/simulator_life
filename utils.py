import random


def random_energy(min_energy: float = 10, max_energy: float = 50) -> float:
    return round(random.uniform(min_energy, max_energy), 1)


def random_name(prefix: str = "Organism") -> str:
    return f"{prefix}_{random.randint(1000, 9999)}"