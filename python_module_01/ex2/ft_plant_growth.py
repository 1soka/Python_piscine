#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {round(self.height, 1)}cm, "
              f"{self.days} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")
    rose: Plant = Plant("rose", 25, 30)
    rose.show()
    start_height: float = rose.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")


if __name__ == "__main__":
    main()
