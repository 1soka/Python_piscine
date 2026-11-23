#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self._height: float = height if height >= 0 else 0.0
        self._days: int = days if days >= 0 else 0

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
            print(f"Height updated: {new_height} cm")

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


def main() -> None:
    print("=== Garden Security System ===")
    rose: Plant = Plant("rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-25)
    rose.set_age(-30)
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
