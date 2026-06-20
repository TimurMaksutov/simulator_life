from ecosystem import Ecosystem
from organism import Animal, Plant


def main() -> None:
    eco = Ecosystem()

    rabbit = Animal("Заяц", energy=50, speed=1.2)
    fox = Animal("Лиса", energy=80, speed=1.5)
    wolf = Animal("Волк", energy=100, speed=1.3)
    grass1 = Plant("Трава1", energy=20, growth_rate=2.5)
    grass2 = Plant("Трава2", energy=25, growth_rate=2.0)
    tree = Plant("Дерево", energy=60, growth_rate=1.0)

    for org in [rabbit, fox, wolf, grass1, grass2, tree]:
        eco.add_organism(org)

    eco.run(days=10)

    print("\n--- Итог ---")
    for org in eco.organisms:
        print(org)


if __name__ == "__main__":
    main()