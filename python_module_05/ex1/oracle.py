#!/usr/bin/env python3
import os


def check_overrides() -> bool:
    from dotenv import load_dotenv
    before_env_terminal: dict[str, str] = dict(os.environ)
    load_dotenv()
    for name, value in before_env_terminal.items():
        if os.environ.get(name) != value:
            print("[WARN] .env overrides environment variables")
            return False
    return True


def check_oracle_env() -> bool:
    env_list: list[str] = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
                           "LOG_LEVEL", "ZION_ENDPOINT"]
    for name in env_list:
        if not os.getenv(name):
            print(f"[WARN] {name} missing: "
                  "the Oracle cannot see all configurations.")
            return False
    return True


def check_hardcore(file_name: str, env_dict: dict[str, str | None]) -> bool:
    count_warn: int = 0
    with open(file_name, "r") as file:
        file_content: str = file.read()
    for name, value in env_dict.items():
        if value and len(value) > 3 and value in file_content:
            print("[WARN] Hardcoded secret detected")
            count_warn += 1
    if count_warn == 0:
        return True
    return False


def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...")
    print()
    try:
        from dotenv import dotenv_values
    except ImportError:
        print("Configuration fail... try again")
        return None
    folder: str = os.path.dirname(__file__)
    print("Configuration loaded:")
    env_dict = dotenv_values(os.path.join(folder, ".env"))
    for name, value in env_dict.items():
        value = os.environ.get(name, value)
        if value and name in ("API_KEY", "DATABASE_URL"):
            value = "********"
        print(f"{name}: {value}")
    print()
    print("Configuration security check:")
    if check_hardcore(__file__, env_dict):
        print("[OK] No hardcoded secrets detected")
    verif_git: int = 0
    try:
        with open(os.path.join(folder, ".gitignore"), "r") as file:
            for line in file:
                if ".env" in line:
                    print("[OK] .env file properly ignored by git")
                    verif_git = 1
                    break
    except FileNotFoundError:
        pass
    if verif_git == 0:
        print("[KO] .env file not ignored by git")
    if check_overrides():
        print("[OK] Production overrides available")
    if check_oracle_env():
        print("The Oracle sees all configurations.")
    return None


if __name__ == "__main__":
    main()
