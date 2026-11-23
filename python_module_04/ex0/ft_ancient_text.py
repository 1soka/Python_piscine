#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return None
    print("=== Cyber Archives Recovery ===")
    file_name: str = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.TextIO = open(file_name, "r")
    except IsADirectoryError as error:
        print(f"IsADirectoryError: {error}")
        return None
    except FileNotFoundError as error:
        print(f"Error opening file '{file_name}': {error}")
        return None
    except PermissionError as error:
        print(f"PermissionError: {error}")
        return None
    print("---\n")
    i = 1
   for line in file:
        print(f"{line}", end="")
        i += 1
    print("\n---")
    file.close()
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
