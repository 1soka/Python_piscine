#!/usr/bin/env python3
import os
import sys
import site


def main() -> None:
    venv_path: str = sys.prefix
    venv_name: str = os.path.basename(venv_path)
    if venv_path == sys.base_prefix:
        print("LABORATORY STATUS: You are working in the open")
        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print()
        print("Global reagent installation path:")
        for path in site.getsitepackages():
            print(path)
        print()
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")

    else:
        print("LABORATORY STATUS: The laboratory is sealed")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}")
        print()
        print("SUCCESS: You are working in an isolated environment!\n"
              "Safe to install reagents without affecting "
              "the global system.")
        print()
        print("Reagent installation path:")
        for path in site.getsitepackages():
            print(path)
    return None


if __name__ == "__main__":
    main()
