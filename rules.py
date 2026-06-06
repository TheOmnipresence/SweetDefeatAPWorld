from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import SweetDefeatWorld


def set_all_rules(world: SweetDefeatWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: SweetDefeatWorld) -> None:
    pass


def set_all_location_rules(world: SweetDefeatWorld) -> None:
    for i in ["Normal", "Invisible", "Pacifism"]:
        set_rule(world.get_location(i + " Level 1"), lambda state: state.has("Level 1 Node", world.player))
        set_rule(world.get_location(i + " Level 2"), lambda state: True)
        set_rule(world.get_location(i + " Level 3"), lambda state: state.has_all(["Level 3 Cooler 1", "Level 3 Cooler 2", "Level 3 Cooler 3"], world.player))
        set_rule(world.get_location(i + " Level 4"), lambda state: state.has_all(["Level 4 Bubble 1", "Level 4 Bubble 2", "Level 4 Bubble 3", "Level 4 Bubble 4"], world.player))
        set_rule(world.get_location(i + " Level 5"), lambda state: state.has_all(["Level 5 Cooler 1", "Level 5 Cooler 2", "Level 5 Cooler 3", "Level 5 Cooler 4", "Level 5 Bubble 3", "Level 5 Bubble 4"], world.player))

    set_rule(world.get_location("Node Level 1"), lambda state: state.has("Level 1 Node", world.player))
    set_rule(world.get_location("Node Level 2"), lambda state: state.has("Level 2 Node", world.player))
    set_rule(world.get_location("Node Level 3"), lambda state: state.has("Level 3 Node", world.player))
    set_rule(world.get_location("Node Level 4"), lambda state: state.has("Level 4 Node", world.player))
    set_rule(world.get_location("Node Level 5"), lambda state: state.has_all(["Level 5 Node", "Level 5 Bubble 3", "Level 5 Bubble 4"], world.player))

    set_rule(world.get_location("Rampage Level 1"), lambda state: True)
    set_rule(world.get_location("Rampage Level 2"), lambda state: True)
    set_rule(world.get_location("Rampage Level 3"), lambda state: True)
    set_rule(world.get_location("Rampage Level 4"), lambda state: True)
    set_rule(world.get_location("Rampage Level 5"), lambda state: True)

    set_rule(world.get_location("Cool Level 1"), lambda state: state.has("Level 1 Cooler 1", world.player))
    set_rule(world.get_location("Cool Level 2"), lambda state: state.has("Level 2 Cooler 1", world.player))
    set_rule(world.get_location("Cool Level 3"), lambda state: state.has_all(["Level 3 Cooler 1", "Level 3 Cooler 2", "Level 3 Cooler 3"], world.player))
    set_rule(world.get_location("Cool Level 4"), lambda state: state.has_all(["Level 4 Cooler 1", "Level 4 Cooler 2", "Level 4 Cooler 3"], world.player))
    set_rule(world.get_location("Cool Level 5"), lambda state: state.has_all(["Level 5 Cooler 1", "Level 5 Cooler 2", "Level 5 Cooler 3", "Level 5 Cooler 4", "Level 5 Bubble 3", "Level 5 Bubble 4"], world.player))


def set_completion_condition(world: SweetDefeatWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Level 5 Node", world.player)
