#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("spell_combiner needs two callable spells")

    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("power_amplifier needs a callable spell")

    def amplified(target: str, power: int) -> str:
        return str(base_spell(target, power * multiplier))
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("conditional_caster needs a callable condition "
                        "and a callable spell")

    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return str(spell(target, power))
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    for spell in spells:
        if not callable(spell):
            raise TypeError("spell_sequence needs a list of callable spells")

    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target}"


def heal(target: str, power: int) -> str:
    return f"Heals {target}"


def lightning(target: str, power: int) -> str:
    return f"Lightning hits {target} for {power} damage"


def power_gauge(target: str, power: int) -> str:
    return str(power)


def main() -> None:
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {', '.join(combined('Dragon', 10))}")

    print("\nTesting power amplifier...")
    mega_gauge = power_amplifier(power_gauge, 3)
    print(f"Original: {power_gauge('Dragon', 10)}, "
          f"Amplified: {mega_gauge('Dragon', 10)}")
    mega_lightning = power_amplifier(lightning, 3)
    print(mega_lightning("Dragon", 10))

    print("\nTesting conditional caster...")
    strong_fireball = conditional_caster(
        lambda target, power: power >= 50, fireball
    )
    print(f"Power 60: {strong_fireball('Dragon', 60)}")
    print(f"Power 20: {strong_fireball('Dragon', 20)}")

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal, lightning])
    for result in combo("Dragon", 25):
        print(result)

    print("\nTesting invalid spell...")
    not_a_spell: Any = "fireball"
    try:
        power_amplifier(not_a_spell, 2)
    except TypeError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
