#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return None
    file_name: str = sys.argv[1]
    if not file_name:
        return None
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.TextIO = open(file_name, "r")
    except FileNotFoundError as error:
        print(f"Error opening file '{file_name}': {error}")
        return None
    except (KeyboardInterrupt, EOFError) as error:
        print(f"EOFError: {error}")
        return None
    except OSError as error:
        print(f"OSError: {error}")
        return None
    print("---\n")
    i = 1
    for line in file:
        print(line, end="")
        i += 1
    print("\n---")
    print(f"File '{file_name}' closed.")
    print("\nTransform data:\n---\n")
    file.close()
    file = open(file_name, "r")
    i = 1
    transformed: list[str] = []
    for line in file:
        new_line = line.rstrip("\n") + "#"
        transformed.append(new_line)
        print(new_line)
        i += 1
    file.close()
    print("\n---")
    try:
        new_file_name: str = input("Enter new file name (or empty): ")
    except EOFError:
        new_file_name = ""
    if not new_file_name:
        print("Not saving data.")
        return None
    try:
        new_file: typing.TextIO = open(new_file_name, "w")
    except OSError as error:
        print(f"OSError: {error}")
        return None
    except (KeyboardInterrupt, EOFError) as error:
        print(f"EOFError: {error}")
        return None
    print(f"Saving data to '{new_file_name}'")
    for line in transformed:
        new_file.write(line + "\n")
    new_file.close()
    print(f"Data saved in file '{new_file_name}'.")


if __name__ == "__main__":
    main()
