#!/usr/bin/env python3


def secure_archive(file_name: str, value: int, content: str
                   ) -> tuple[bool, str] | None:
    if not file_name:
        return None
    if value < 0 or value > 1:
        return None
    type_file: str = "r" if value == 0 else "w"
    content_read: str = ""
    value_error: str = ""
    try:
        with open(file_name, type_file) as file:
            if value == 0:
                content_read += file.read()
            else:
                for line in content.split("\n"):
                    file.write(line)
    except FileNotFoundError as error:
        value_error = str(error)
    except PermissionError as error:
        value_error = str(error)
    except IsADirectoryError as error:
        value_error = str(error)
    if not value_error:
        return (False, value_error)
    else:
        if value == 0:
            return (True, content_read)
        else:
            return (True, "Content successfully written to file")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 1, ""))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", 1, ""))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("content.txt", 1, ""))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("content.txt", 2, "Ceci est un petit test !"))


if __name__ == "__main__":
    main()
