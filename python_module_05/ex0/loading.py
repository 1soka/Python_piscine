#!/usr/bin/env python3
from importlib import import_module, metadata


def main() -> None:
    module_dict: dict[str, str] = {
            "pandas": "Data manipulation ready",
            "numpy": "Numerical computation ready"
            }
    print()
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")
    count_missing: int = 0
    for module, description in module_dict.items():
        try:
            import_module(module)
            version: str = metadata.version(module)
            print(f"[OK] {module} ({version}) - {description}")
        except ImportError:
            print(f"[KO] {module}: missing dependencies.")
            count_missing += 1
    print()
    if count_missing > 0:
        print("Install dependencies with pip: ")
        print("- pip install -r ex0/requirements.txt")
        print("- python3 ex0/loading.py")
        print()
        print("Install dependencies with Poetry: ")
        print("- cd ex0 && poetry install")
        print("- poetry run python loading.py")
    else:
        print("pip vs Poetry:")
        print("  requirements.txt declares what to install; "
              "pip resolves it at install time.")
        print("  pyproject.toml declares the same constraints, and Poetry "
              "pins the resolved")
        print("  versions in poetry.lock so every install is identical.")
        print()
        print("All reagents present and accounted for.")
    return None


if __name__ == "__main__":
    main()
