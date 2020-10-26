import math


def gimmePizza(team, slices_in_pizza):
    print(team, slices_in_pizza)

    total_slices = sum([person["num"] for person in team ])

    print(f"Total slices: {total_slices}")

    needed = total_slices / slices_in_pizza
    if needed.is_integer():
        return needed
    else:
        return math.floor(needed) + 1


if __name__ == '__main__':
    print(gimmePizza([{"name": "Joe", "num": 9}, {"name": "Cami", "num": 3}, {"name": "Cassidy", "num": 4}], 8))
    print()
    print(gimmePizza([{"name": "Joe", "num": 10}, {"name": "Cami", "num": 3}, {"name": "Cassidy", "num": 4}], 9))
    print()
    print(gimmePizza([{"name": "Joe", "num": 11}, {"name": "Cami", "num": 13}, {"name": "Cassidy", "num": 4}], 10))

    # add more test cases...
