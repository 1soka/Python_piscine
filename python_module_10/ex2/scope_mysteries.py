#!/usr/bin/env python3
from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count: int = 0

    def count_incrementation() -> int:
        nonlocal count
        count += 1
        return count
    return count_incrementation


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def add_spell(power: int) -> int:
        nonlocal total
        total += power
        return total
    return add_spell


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a: Callable[[], int] = mage_counter()
    counter_b: Callable[[], int] = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()
    print("Testing spell accumulator...")
    accumulator: Callable[[int], int] = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")
    print()
    print("Testing enchantment factory...")
    flaming: Callable[[str], str] = enchantment_factory("Flaming")
    frozen: Callable[[str], str] = enchantment_factory("Frozen")
    print(f"{flaming('Sword')}\n{frozen('Shield')}")
    print()
    print("Testing memory vault...")
    vault: dict[str, Callable] = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
    return None


if __name__ == "__main__":
    main()
