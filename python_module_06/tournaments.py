#!/usr/bin/env python3
from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory
from ex4 import (AggressiveStrategy, BattleStrategy, InvalidStrategyError,
                 NormalStrategy)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_a, strategy_a = opponents[i]
                factory_b, strategy_b = opponents[j]
                fighter_a = factory_a.create_base()
                fighter_b = factory_b.create_base()
                print()
                print("* Battle *")
                print(fighter_a.describe())
                print(" vs.")
                print(fighter_b.describe())
                print(" now fight!")
                strategy_a.act(fighter_a)
                strategy_b.act(fighter_b)
    except InvalidStrategyError as error:
        print(f"Battle error, aborting tournament: {error}")


def main() -> None:
    flame = FlameFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    tournaments: list[tuple[str, list[tuple[CreatureFactory,
                                            BattleStrategy]]]] = [
        ("basic", [(flame, normal), (transform, aggressive)]),
        ("error", [(transform, aggressive), (flame, aggressive)]),
    ]
    for index, (label, opponents) in enumerate(tournaments):
        if index > 0:
            print()
        print(f"Tournament {index} ({label})")
        names = [f"({factory.create_base().name}+{strategy.name})"
                 for factory, strategy in opponents]
        print(f" [ {', '.join(names)} ]")
        battle(opponents)


if __name__ == "__main__":
    main()
