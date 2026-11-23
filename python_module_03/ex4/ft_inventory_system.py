#!/usr/bin/env python3
import sys


def get_list_item(input_list: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for value in input_list[1:]:
        try:
            value_name, value_item = value.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{value}'")
            continue
        if value_name in inventory:
            print(f"Redundant item '{value_name}' - discarding")
            continue
        try:
            inventory[value_name] = int(value_item)
        except ValueError as error:
            print(f"Quantity error for '{value_name}': {error}")
            continue
    return inventory


def get_extreme_value(inventory: dict[str, int]) -> list[str]:
    keys: list[str] = list(inventory.keys())
    most: str = keys[0]
    least: str = keys[0]
    for key in keys:
        if inventory[key] > inventory[most]:
            most = key
        if inventory[key] < inventory[least]:
            least = key
    return [most, least]


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = get_list_item(sys.argv)
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    if len(inventory) == 0:
        print("Inventory is empty bro...")
        return
    print(f"Total quantity of the {len(inventory)} ",
          "items: {sum(inventory.values())}")
    for item in inventory:
        value = inventory[item]
        pourcent = round(value / sum(inventory.values()) * 100, 1)
        print(f"Item {item} represents {pourcent}%")
    most_key, least_key = get_extreme_value(inventory)
    print(f"Item most abundant: {most_key} with ",
          "quantity {inventory[most_key]}")
    print(f"Item least abundant: {least_key} with ",
          "quantity {inventory[least_key]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
