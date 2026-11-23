#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    for data in ("25", "abc"):
        print()
        print(f"Input data is '{data}'")
        try:
            temp: int = input_temperature(data)
            print(f"Temperature is now {temp}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
    print()
    print("All tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
