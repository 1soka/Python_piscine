#!/usr/bin/env python3
import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    list_player: list[str] = [
        "Andy", "Kendy", "Yacine", "Basit", "Maxime",
        "Mael", "Abdel", "Nathan", "Elliot"
    ]
    list_action: list[str] = [
        "Valgrind Error",
        "Full box -200",
        "Feinte ronaldo prime",
        "Degrader spas-12",
        "Triple salto arriere",
        "Compilation gcc",
        "Faille XSS by ???",
        "Kebs sauce blanche harissa",
        "Transendance correction 8h"
    ]
    while True:
        player = random.choice(list_player)
        action = random.choice(list_action)
        yield (player, action)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        index = random.randrange(len(events))
        element = events.pop(index)
        yield element


def main() -> None:
    print("=== Game Data Stream Processor ===")
    generation = gen_event()
    for i in range(1000):
        event = next(generation)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    events_list: list[tuple[str, str]] = [next(generation) for _ in range(10)]
    print(f"Built list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
