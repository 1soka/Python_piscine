#!/usr/bin/env python3
import operator
from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    if not spells:
        return 0
    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, power=50, element="Fire"),
        "ice": partial(base_enchantment, power=50, element="Ice"),
        "lightning": partial(base_enchantment, power=50, element="Lightning"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


def enchant(power: int, element: str, target: str) -> str:
    return f"{element} enchantment hits {target} with {power} power"


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")
    print(f"Empty: {spell_reducer([], 'add')}")
    try:
        spell_reducer(spells, "divide")
    except ValueError as error:
        print(f"Error: {error}")

    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(enchant)
    for name, enchantment in enchantments.items():
        print(f"{name}: {enchantment(target='Dragon')}")

    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast(["fireball", "heal", "shield"]))
    print(cast(3.14))


if __name__ == "__main__":
    main()
