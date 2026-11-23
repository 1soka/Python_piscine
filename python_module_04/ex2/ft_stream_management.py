#!/usr/bin/env python3
import sys
import typing


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) == 1:
        print("Usage: ft_stream_management.py <file>")
        return None
    file_name: str = sys.argv[1]
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.TextIO = open(file_name, "r")
    except OSError as error:
        print(f"[STDERR] Error opening file '{file_name}': {error}",
              file=sys.stderr)
        print("Data not saved.")
        return None
    except PermissionError as error:
        print(f"[STDERR] {error}", file=sys.stderr)
        return None
    print("---\n")
    i = 1
    for line in file:
        print(f"{line}", end="")
        i += 1
    print("\n---")
    file.close()
    print(f"File '{file_name}' closed.")
    print("\nTransform data:\n---\n")
    file = open(file_name, "r")
    i = 1
    lines: list[str] = []
    for line in file:
        new_line = line.rstrip("\n") + "#"
        lines.append(new_line)
        print(f"{new_line}")
        i += 1
    file.close()
    print("\n---")
    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    new_file_name: str = sys.stdin.readline().strip()
    if not new_file_name:
        print("Not saving data.")
        return None
    print(f"Saving data to '{new_file_name}'")
    try:
        new_file: typing.TextIO = open(new_file_name, "w")
    except OSError as error:
        print(f"[STDERR] Error opening file '{file_name}': {error}",
              file=sys.stderr)
        print("Data not saved.")
        return None
    except PermissionError as error:
        print(f"PermissionError: {error}")
        return None
    for line in lines:
        new_file.write(line + "\n")
    new_file.close()
    print(f"Data saved in file '{new_file_name}'.")


if __name__ == "__main__":
    main()
