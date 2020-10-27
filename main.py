import math


def gimmePizza(team, slices_in_pizza):
    print(team, slices_in_pizza)
    if slices_in_pizza <= 0:
        return 0

    total_slices = sum([person["num"] for person in team ])

    print(f"Total slices: {total_slices}")

    needed = total_slices / slices_in_pizza
    if needed.is_integer():
        return needed
    else:
        return math.floor(needed) + 1
