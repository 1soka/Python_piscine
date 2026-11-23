#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self._name: str = name
        self._height: float = height
        self._days: int = days

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._days += 1

    def show(self) -> None:
        print(f"Created: {self._name.capitalize()}: {round(self._height, 1)}"
              f"cm, {self._days} days old")


def main() -> None:
    print("=== Plant Factory Output ===")
    list_plants: list[Plant] = [
        Plant("rose", 25, 30),
        Plant("oak", 200, 365),
        Plant("cactus", 5, 90),
        Plant("sunflower", 80, 45),
        Plant("fern", 15, 120)
            ]
    for plant in list_plants:
        plant.show()


if __name__ == "__main__":
    main()
