def ft_count_harvest_recursive(day: int = 1, total: int = 0) -> None:
    if total == 0:
        total = int(input("Days until harvest: "))
    if day > total:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(day + 1, total)
