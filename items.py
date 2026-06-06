from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .locations import map_to_dict

if TYPE_CHECKING:
    from .world import SweetDefeatWorld

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
LEVEL_ITEMS = [
    "Level 1 Node",
    "Level 1 Cooler 1",

    "Level 2 Node",
    "Level 2 Cooler 1",

    "Level 3 Node",
    "Level 3 Cooler 1",
    "Level 3 Cooler 2",
    "Level 3 Cooler 3",

    "Level 4 Node",
    "Level 4 Cooler 1",
    "Level 4 Cooler 2",
    "Level 4 Cooler 3",
    "Level 4 Bubble 1",
    "Level 4 Bubble 2",
    "Level 4 Bubble 3",
    "Level 4 Bubble 4",

    "Level 5 Node",
    "Level 5 Cooler 1",
    "Level 5 Cooler 2",
    "Level 5 Cooler 3",
    "Level 5 Cooler 4",
    "Level 5 Bubble 1",
    "Level 5 Bubble 2",
    "Level 5 Bubble 3",
    "Level 5 Bubble 4",
]

ITEM_NAME_TO_ID = {"Quack": 1000} | map_to_dict(LEVEL_ITEMS, lambda e: LEVEL_ITEMS.index(e) + 1)

DEFAULT_ITEM_CLASSIFICATIONS = {"Quack": ItemClassification.filler} | map_to_dict(LEVEL_ITEMS, lambda e: ItemClassification.progression)


class SweetDefeatItem(Item):
    game = "Sweet Defeat"


def get_random_filler_item_name(world: SweetDefeatWorld) -> str:
    return "Quack"


def create_item_with_correct_classification(world: SweetDefeatWorld, name: str) -> SweetDefeatItem:
    return SweetDefeatItem(name, DEFAULT_ITEM_CLASSIFICATIONS[name], ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: SweetDefeatWorld) -> None:
    itempool: list[Item] = []
    for i in LEVEL_ITEMS:
        itempool.append(world.create_item(i))

    number_of_items = len(itempool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool
