#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self._height: float = height if height >= 0 else 0.0
        self._days: int = days if days >= 0 else 0

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self._height:.1f}cm,"
              f" {self._days} days old")

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._days += 1

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days

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


class Flower(Plant):
    def __init__(self, name: str, height: float, days: int) -> None:
        super().__init__(name, height, days)
        self.color: str = "red"
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
    def __init__(self, name: str, height: float, days: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, days)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, days: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, days)
        self.harvest_season: str = harvest_season
        self.nutritional_value: float = 0.0

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {round(self.nutritional_value)}")

    def grow(self) -> None:
        super().grow()
        self._height += 1.3
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5


def main() -> None:
    print("=== Garden Plant Types ===")
    rose: Flower = Flower("rose", 15.0, 10)
    oak: Tree = Tree("oak", 200.0, 365, 5.0)
    tomato: Vegetable = Vegetable("tomato", 5.0, 10, "April")
    print("=== Flower")
    for blooming in (False, True):
        rose.blooming = blooming
        if rose.blooming:
            print("[asking the rose to bloom]")
        rose.show()
        print(f"Color: {rose.color}")
        rose.bloom()
    print()
    print("=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()
    print("=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
