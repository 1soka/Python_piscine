def ft_harvest_total():
    value = 0
    for i in range(1, 4):
        value += int(input(f"Day {i} harvest: "))
    print(f"Total harvest: {value}")
