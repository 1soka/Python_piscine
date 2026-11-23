#!/usr/bin/env python3
import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        value: str = input("Enter new coordinates as floats "
                           "in format 'x,y,z': ")
        try:
            x_str, y_str, z_str = value.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        try:
            for part in (x_str, y_str, z_str):
                float(part)
        except ValueError as error:
            print(f"Error on parameter '{part.strip()}': {error}")
            continue
        return (float(x_str), float(y_str), float(z_str))


def distance(a: tuple[float, float, float],
             b: tuple[float, float, float]) -> float:
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
                                        + (b[2] - a[2]) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first: tuple[float, float, float] = get_player_pos()
    x, y, z = first
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {round(distance((0, 0, 0), first), 4)}")
    print("Get a second set of coordinates")
    second: tuple[float, float, float] = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(distance(first, second), 4)}")


if __name__ == "__main__":
    main()
