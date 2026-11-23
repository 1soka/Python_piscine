#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    rose: Plant = Plant("rose", 25, 30)
    sunflower: Plant = Plant("sunflower", 25, 30)
    cactus: Plant = Plant("cactus", 25, 30)
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
