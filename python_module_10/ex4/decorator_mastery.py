#!/usr/bin/env python3
import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        right_now: float = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"Spell completed in "
              f"{time.perf_counter() - right_now:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if "power" in kwargs:
                power = kwargs["power"]
            else:
                power = args[-1]
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@power_validator(20)
def ice_storm(target: str, power: int) -> str:
    return f"Ice storm freezes {target} with {power} power"


@retry_spell(3)
def unstable_spell() -> str:
    raise RuntimeError("The spell collapsed")


@retry_spell(3)
def war_cry() -> str:
    return "Waaaaaaagh spelled !"


def main() -> None:
    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting power validator...")
    print(ice_storm("Goblin", 25))
    print(ice_storm("Goblin", power=5))

    print("\nTesting retrying spell...")
    print(unstable_spell())
    print(war_cry())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Merlin the Wise"))
    print(MageGuild.validate_mage_name("X1"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))


if __name__ == "__main__":
    main()
