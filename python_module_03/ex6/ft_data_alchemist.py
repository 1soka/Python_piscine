#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    list_player: list[str] = [
        'Alice',
        'bob',
        'Charlie',
        'dylan',
        'Emma',
        'Gregory',
        'john',
        'kevin',
        'Liam'
    ]
    print("\n")
    print(f"Initial list of players: {list_player}")
    list_player_upper: list[str] = []
    list_player_lower: list[str] = []
    for player in list_player:
        if player[0].isupper():
            list_player_upper.append(player)
        else:
            list_player_lower.append(player)
    list_all_maj: list[str] = [p.capitalize() for p in list_player]
    print(f"New list with all names capitalized: {list_all_maj}")
    print(f"New list of capitalized names only: {list_player_upper}")
    dict_scores: dict[str, int] = {
        name: random.randint(0, 1000) for name in list_player_upper
    }
    if len(dict_scores) == 0:
        return None
    moyenne = sum(dict_scores.values()) / len(dict_scores)
    dict_top_scores: dict[str, int] = {
        name: score for name, score in dict_scores.items() if score > moyenne
    }
    print(f"Score dict : {dict_scores}")
    print(f"Score average is {round(moyenne, 2)}")
    print(f"High scores : {dict_top_scores}")


if __name__ == "__main__":
    main()
