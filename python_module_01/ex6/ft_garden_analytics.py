#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self._height: float = height if height >= 0 else 0.0
        self._days: int = days if days >= 0 else 0
        self._stats: Plant.Stats = self.Stats()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        plant_unknown: "Plant" = cls("Unknown plant", 0.0, 0)
        return plant_unknown

    def grow(self, value: float) -> None:
        self._height += value
        self._stats.add_grow()

    def age(self, value: int) -> None:
        self._days += value
        self._stats.add_age()

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

    def get_stats(self) -> "Plant.Stats":
        return self._stats

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = new_age
            print(f"Age updated: {new_age} days")

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self._height:.1f}cm,"
              f" {self._days} days old")
        self._stats.add_show()

    class Stats:
        def __init__(self) -> None:
            self._grow: int = 0
            self._age: int = 0
            self._show: int = 0

        def add_grow(self) -> None:
            self._grow += 1

        def add_age(self) -> None:
            self._age += 1

        def add_show(self) -> None:
            self._show += 1

        def display(self) -> None:
            print(f"Stats: {self._grow} grow, {self._age} age, "
                  f"{self._show} show")
            return None


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int,
                 color: str) -> None:
        super().__init__(name, height, days)
        self.color: str = color
        self.blooming: bool = False

    def bloom(self) -> None:
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.blooming:
            print(f"{self.name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self.name.capitalize()} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade: int = 0

        def add_shade(self) -> None:
            self._shade += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade} shade")

    _stats: Stats

    def __init__(self, name: str, height: float, days: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")
        self._stats.add_shade()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, days)
        self.harvest_season: str = harvest_season
        self.nutritional_value: float = 0.0

    def grow(self, amount: float = 2.1) -> None:
        super().grow(amount)
        self.nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {round(self.nutritional_value)}")


class Seed(Flower):
    def __init__(self, name: str, height: float, days: int,
                 color: str, seeds: int) -> None:
        super().__init__(name, height, days, color)
        self._seeds_to_give: int = seeds
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = self._seeds_to_give

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    stats: Plant.Stats = plant.get_stats()
    stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> "
          f"{Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose: Flower = Flower("rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_stats(rose)
    print()

    print("=== Tree")
    oak: Tree = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print()

    print("=== Seed")
    sunflower: Seed = Seed("sunflower", 80.0, 45, "yellow", 42)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print()

    print("=== Anonymous")
    unknown: Plant = Plant.anonymous()
    unknown.show()
    display_stats(unknown)


if __name__ == "__main__":
    main()
