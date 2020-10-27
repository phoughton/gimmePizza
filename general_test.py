import pytest
from main import *


@pytest.mark.parametrize("team, slices_in_pizza, pizzas_required", [
        ([{"name": "Joe", "num": 9},  {"name": "Cami", "num": 3},   {"name": "Cassidy", "num": 4}], 8, 2),
        ([{"name": "Joe", "num": 10}, {"name": "Cami", "num": 3},   {"name": "Cassidy", "num": 4}], 9, 2),
        ([{"name": "Joe", "num": 11}, {"name": "Cami", "num": 13},  {"name": "Cassidy", "num": 4}], 8, 4),
        ([], 8, 0),
        ([], 0, 0),
        ([{"name": "Joe", "num": 10}], 9, 2),
        ([{"name": "Jowdewfwegwrvwrvwrve", "num": 242342345}], 1, 242342345),
        ([{"name": "Jowdewfwegwrvwrvwrve", "num": 242342345}], 5, 48468469),
        ([{"name": "Joe", "num": 1}, {"name": "Cami", "num": 1},  {"name": "Cassidy", "num": 1}], 3, 1)
])
def test_examples_straight_forward(team, slices_in_pizza, pizzas_required):
    pizzas_calculated = gimmePizza(team, slices_in_pizza)
    print(f"pizzas_required: {pizzas_required}, pizzas_calculated: {pizzas_calculated}, team: {team}, slices_in_pizza:{slices_in_pizza}")
    assert pizzas_calculated == pizzas_required, \
        f"pizzas_required: {pizzas_required}, pizzas_calculated: {pizzas_calculated}," +\
        f"team: {team}, slices_in_pizza:{slices_in_pizza}" \
