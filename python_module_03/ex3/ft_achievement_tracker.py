#!/usr/bin/env python3
import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "World Savior", "Master Explorer",
    "Collector Supreme", "Untouchable", "Boss Slayer", "Strategist",
    "Unstoppable", "Speed Runner", "Survivor", "Treasure Hunter",
    "First Steps", "Sharp Mind", "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count: int = random.randint(8, 11)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    players: list[tuple[str, set[str]]] = [
        ("Alice", gen_player_achievements()),
        ("Bob", gen_player_achievements()),
        ("Charlie", gen_player_achievements()),
        ("Dylan", gen_player_achievements()),
    ]
    all_achievements: set[str] = set()
    common: set[str] = players[0][1]
    for name, achievements in players:
        print(f"Player {name}: {achievements}")
        all_achievements = all_achievements.union(achievements)
        common = common.intersection(achievements)
    print(f"All distinct achievements: {all_achievements}")
    print(f"Common achievements: {common}")
    for name, achievements in players:
        others: set[str] = set()
        for other_name, other_achievements in players:
            if other_name != name:
                others = others.union(other_achievements)
        print(f"Only {name} has: {achievements.difference(others)}")
    for name, achievements in players:
        print(f"{name} is missing: "
              f"{all_achievements.difference(achievements)}")


if __name__ == "__main__":
    main()
