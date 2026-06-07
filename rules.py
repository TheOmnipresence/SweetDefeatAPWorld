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
    for i in ["Normal", "Invisible", "Pacifism", "Normal 2"]:
        set_rule(world.get_location(i + " Level 1"), lambda state: state.has("Level 1 Node", world.player))
        set_rule(world.get_location(i + " Level 2"), lambda state: True)
        set_rule(world.get_location(i + " Level 3"), lambda state: state.has_all(["Level 3 Cooler 1", "Level 3 Cooler 2", "Level 3 Cooler 3"], world.player))
        set_rule(world.get_location(i + " Level 4"), lambda state: state.has_all(["Level 4 Bubble 1", "Level 4 Bubble 2", "Level 4 Bubble 3", "Level 4 Bubble 4"], world.player))
        set_rule(world.get_location(i + " Level 5"), lambda state: state.has_all(["Level 5 Cooler 1", "Level 5 Cooler 2", "Level 5 Cooler 3", "Level 5 Cooler 4", "Level 5 Bubble 2", "Level 5 Bubble 3", "Level 5 Bubble 4"], world.player))
        set_rule(world.get_location(i + " Level 6"), lambda state: (state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or state.has("Level 6 Bubble 4", world.player))
        set_rule(world.get_location(i + " Level 7"), lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or state.has("Level 7 Bubble 4", world.player)) and state.has_all(["Level 7 Bubble 9", "Level 7 Cooler 1", "Level 7 Cooler 2"], world.player))
        set_rule(world.get_location(i + " Level 8"), lambda state: ((state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or state.has("Level 8 Bubble 4", world.player)) and state.has_all(["Level 8 Bubble 9", "Level 8 Bubble 11"], world.player))
        set_rule(world.get_location(i + " Level 9"), lambda state: state.has_any(["Level 9 Cooler 1", "Level 9 Cooler 2"], world.player))
        set_rule(world.get_location(i + " Level 10"), lambda state: state.has_all(["Level 10 Cooler 1", "Level 10 Cooler 2", "Level 10 Cooler 3", "Level 10 Bubble 9"], world.player))
        set_rule(world.get_location(i + " Level 11"), lambda state: True)
        set_rule(world.get_location(i + " Level 12"), lambda state: state.has_all(["Level 12 Cooler 1", "Level 12 Cooler 2"], world.player))
        set_rule(world.get_location(i + " Level 13"), lambda state: True)
        set_rule(world.get_location(i + " Level 14"), lambda state: state.has_all(["Level 14 Bubble 1", "Level 14 Cooler 2"], world.player) or state.has_all(["Level 14 Bubble " + str(bubble + 2) for bubble in range(6)] + ["Level 14 Cooler 1"], world.player))
        set_rule(world.get_location(i + " Level 15"), lambda state: state.has_all(["Level 15 Cooler " + str(cooler + 1) for cooler in range(3)], world.player))

    set_rule(world.get_location("Node Level 1"), lambda state: state.has("Level 1 Node", world.player))
    set_rule(world.get_location("Node Level 2"), lambda state: state.has("Level 2 Node", world.player))
    set_rule(world.get_location("Node Level 3"), lambda state: state.has("Level 3 Node", world.player))
    set_rule(world.get_location("Node Level 4"), lambda state: state.has("Level 4 Node", world.player))
    set_rule(world.get_location("Node Level 5"), lambda state: state.has_all(["Level 5 Node", "Level 5 Bubble 2", "Level 5 Bubble 3", "Level 5 Bubble 4"], world.player))
    set_rule(world.get_location("Node Level 6"), lambda state: ((state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or state.has("Level 6 Bubble 4", world.player)) and state.has("Level 1 Node", world.player))
    set_rule(world.get_location("Node Level 7"), lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or state.has("Level 7 Bubble 4", world.player)) and state.has_all(["Level 7 Bubble 9", "Level 7 Node"], world.player))
    set_rule(world.get_location("Node Level 8"), lambda state: ((state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or state.has("Level 8 Bubble 4", world.player)) and state.has_all(["Level 8 Bubble 9", "Level 8 Bubble 11", "Level 8 Node"], world.player))
    set_rule(world.get_location("Node Level 9"), lambda state: state.has("Level 9 Node", world.player))
    set_rule(world.get_location("Node Level 10"), lambda state: state.has("Level 10 Node", world.player))
    set_rule(world.get_location("Node Level 11"), lambda state: state.has("Level 11 Node", world.player))
    set_rule(world.get_location("Node Level 12"), lambda state: state.has("Level 12 Node", world.player))
    set_rule(world.get_location("Node Level 13"), lambda state: state.has("Level 13 Node", world.player))
    set_rule(world.get_location("Node Level 14"), lambda state: state.has("Level 14 Node", world.player))
    set_rule(world.get_location("Node Level 15"), lambda state: state.has("Level 15 Node", world.player))

    set_rule(world.get_location("Rampage Level 1"), lambda state: True)
    set_rule(world.get_location("Rampage Level 2"), lambda state: True)
    set_rule(world.get_location("Rampage Level 3"), lambda state: True)
    set_rule(world.get_location("Rampage Level 4"), lambda state: True)
    set_rule(world.get_location("Rampage Level 5"), lambda state: True)
    set_rule(world.get_location("Rampage Level 6"), lambda state: (state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or state.has("Level 6 Bubble 4", world.player))
    set_rule(world.get_location("Rampage Level 7"), lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or state.has("Level 7 Bubble 4", world.player)) and state.has("Level 7 Bubble 9", world.player))
    set_rule(world.get_location("Rampage Level 8"), lambda state: ((state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or state.has("Level 8 Bubble 4", world.player)) and state.has_all(["Level 8 Bubble 9", "Level 8 Bubble 11"], world.player))
    set_rule(world.get_location("Rampage Level 9"), lambda state: state.has_any(["Level 9 Cooler 1", "Level 9 Cooler 2", "Level 9 Bubble 9", "Level 9 Bubble 11"], world.player))
    set_rule(world.get_location("Rampage Level 10"), lambda state: state.has("Level 10 Cooler 1", world.player))
    set_rule(world.get_location("Rampage Level 11"), lambda state: True)
    set_rule(world.get_location("Rampage Level 12"), lambda state: True)
    set_rule(world.get_location("Rampage Level 13"), lambda state: True)
    set_rule(world.get_location("Rampage Level 14"), lambda state: True)
    set_rule(world.get_location("Rampage Level 15"), lambda state: True)

    set_rule(world.get_location("Cool Level 1"), lambda state: state.has("Level 1 Cooler 1", world.player))
    set_rule(world.get_location("Cool Level 2"), lambda state: state.has("Level 2 Cooler 1", world.player))
    set_rule(world.get_location("Cool Level 3"), lambda state: state.has_all(["Level 3 Cooler 1", "Level 3 Cooler 2", "Level 3 Cooler 3"], world.player))
    set_rule(world.get_location("Cool Level 4"), lambda state: state.has_all(["Level 4 Cooler 1", "Level 4 Cooler 2", "Level 4 Cooler 3"], world.player))
    set_rule(world.get_location("Cool Level 5"), lambda state: state.has_all(["Level 5 Cooler 1", "Level 5 Cooler 2", "Level 5 Cooler 3", "Level 5 Cooler 4", "Level 5 Bubble 3", "Level 5 Bubble 4"], world.player))
    set_rule(world.get_location("Cool Level 6"), lambda state: ((state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or state.has("Level 6 Bubble 4", world.player)) and state.has("Level 6 Cooler 1", world.player))
    set_rule(world.get_location("Cool Level 7"), lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or state.has("Level 7 Bubble 4", world.player)) and state.has_all(["Level 7 Bubble 9", "Level 7 Cooler 1", "Level 7 Cooler 2"], world.player))
    set_rule(world.get_location("Cool Level 8"), lambda state: ((state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or state.has("Level 8 Bubble 4", world.player)) and state.has_all(["Level 8 Bubble 9", "Level 8 Cooler 1", "Level 8 Cooler 2"], world.player))
    set_rule(world.get_location("Cool Level 9"), lambda state: state.has_all(["Level 9 Cooler 1", "Level 9 Cooler 2"], world.player))
    set_rule(world.get_location("Cool Level 10"), lambda state: state.has_all(["Level 10 Cooler 1", "Level 10 Cooler 2", "Level 10 Cooler 3", "Level 10 Bubble 9"], world.player))
    set_rule(world.get_location("Cool Level 11"), lambda state: state.has("Level 11 Cooler 1", world.player))
    set_rule(world.get_location("Cool Level 12"), lambda state: state.has_all(["Level 12 Cooler 1", "Level 12 Cooler 2"], world.player))
    set_rule(world.get_location("Cool Level 13"), lambda state: state.has_all(["Level 13 Cooler 1", "Level 13 Cooler 2"], world.player))
    set_rule(world.get_location("Cool Level 14"), lambda state: state.has_all(["Level 14 Cooler 1", "Level 14 Cooler 2"], world.player))
    set_rule(world.get_location("Cool Level 15"), lambda state: state.has_all(["Level 15 Cooler 1", "Level 15 Cooler 2", "Level 15 Cooler 3"], world.player))

    set_rule(world.get_location("Void Level 1"), lambda state: True)
    set_rule(world.get_location("Void Level 2"), lambda state: True)
    set_rule(world.get_location("Void Level 3"), lambda state: True)
    set_rule(world.get_location("Void Level 4"), lambda state: True)
    set_rule(world.get_location("Void Level 5"), lambda state: True)
    set_rule(world.get_location("Void Level 6"), lambda state: True)
    set_rule(world.get_location("Void Level 7"), lambda state: True)
    set_rule(world.get_location("Void Level 8"), lambda state: True)
    set_rule(world.get_location("Void Level 9"), lambda state: True)
    set_rule(world.get_location("Void Level 10"), lambda state: True)
    set_rule(world.get_location("Void Level 11"), lambda state: True)
    set_rule(world.get_location("Void Level 12"), lambda state: True)
    set_rule(world.get_location("Void Level 13"), lambda state: True)
    set_rule(world.get_location("Void Level 14"), lambda state: True)
    set_rule(world.get_location("Void Level 15"), lambda state: True)

    set_rule(world.get_location("Easier Level 1"), lambda state: state.has("Level 1 Node", world.player))
    set_rule(world.get_location("Easier Level 2"), lambda state: True)
    set_rule(world.get_location("Easier Level 3"), lambda state: state.has_from_list_unique(["Level 3 Cooler 1", "Level 3 Cooler 2", "Level 3 Cooler 3"], world.player, 2))
    set_rule(world.get_location("Easier Level 4"), lambda state: state.has_from_list_unique(["Level 4 Bubble 1", "Level 4 Bubble 2", "Level 4 Bubble 3", "Level 4 Bubble 4"], world.player, 2))
    set_rule(world.get_location("Easier Level 5"), lambda state: state.has_from_list_unique(["Level 5 Bubble 1", "Level 5 Bubble 2", "Level 5 Bubble 3", "Level 5 Bubble 4"], world.player, 3) and state.has_from_list_unique(["Level 5 Cooler 1", "Level 5 Cooler 2", "Level 5 Cooler 3"], world.player, 2)) #TODO
    set_rule(world.get_location("Easier Level 6"), lambda state: (state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or state.has("Level 6 Bubble 4", world.player))
    set_rule(world.get_location("Easier Level 7"), lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or state.has("Level 7 Bubble 4", world.player)) and state.has("Level 7 Bubble 9", world.player) and state.has_any(["Level 7 Cooler 1", "Level 7 Cooler 2"], world.player))
    set_rule(world.get_location("Easier Level 8"), lambda state: ((state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or state.has("Level 8 Bubble 4", world.player)) and state.has("Level 8 Bubble 9", world.player))
    set_rule(world.get_location("Easier Level 9"), lambda state: state.has_any(["Level 9 Cooler 1", "Level 9 Cooler 2"], world.player))
    set_rule(world.get_location("Easier Level 10"), lambda state: (state.has_all(["Level 10 Cooler 1", "Level 10 Cooler 3"], world.player) or state.has_all(["Level 10 Cooler 1", "Level 10 Cooler 2", "Level 10 Bubble 9"], world.player) or state.has_all(["Level 10 Cooler 3", "Level 10 Cooler 2", "Level 10 Bubble 9"], world.player)) and state.has_from_list_unique(["Level 10 Bubble " + str(bubble + 1) for bubble in range(11)], world.player, 3))
    set_rule(world.get_location("Easier Level 11"), lambda state: True)
    set_rule(world.get_location("Easier Level 12"), lambda state: state.has_any(["Level 12 Cooler 1", "Level 12 Cooler 2"], world.player))
    set_rule(world.get_location("Easier Level 13"), lambda state: state.has_any(["Level 12 Cooler 1", "Level 12 Cooler 2"], world.player))
    set_rule(world.get_location("Easier Level 14"), lambda state: state.has_all(["Level 12 Bubble 1", "Level 12 Cooler 2"], world.player) or state.has_all(["Level 12 Bubble 2", "Level 12 Cooler 1"], world.player))
    set_rule(world.get_location("Easier Level 15"), lambda state: state.has_from_list_unique(["Level 15 Cooler " + str(cooler + 1) for cooler in range(3)], world.player, 2) and state.has_from_list_unique(["Level 15 Bubble " + str(cooler + 1) for cooler in range(7)], world.player, 2))

    set_rule(world.get_location("One Level 1"), lambda state: state.has("Level 1 Node", world.player))
    set_rule(world.get_location("One Level 2"), lambda state: True)
    set_rule(world.get_location("One Level 3"), lambda state: state.has_any(["Level 3 Cooler 1", "Level 3 Cooler 2", "Level 3 Cooler 3"], world.player))
    set_rule(world.get_location("One Level 4"), lambda state: state.has_any(["Level 4 Bubble 1", "Level 4 Bubble 2", "Level 4 Bubble 3", "Level 4 Bubble 4"], world.player))
    set_rule(world.get_location("One Level 5"), lambda state: state.has_any(["Level 5 Cooler 1", "Level 5 Cooler 2", "Level 5 Cooler 3"], world.player) or state.has_all(["Level 5 Bubble 2", "Level 5 Bubble 3", "Level 5 Bubble 4", "Level 5 Cooler 4"], world.player))
    set_rule(world.get_location("One Level 6"), lambda state: (state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or state.has("Level 6 Bubble 4", world.player))
    set_rule(world.get_location("One Level 7"), lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or state.has("Level 7 Bubble 4", world.player)) and state.has_any(["Level 7 Cooler 1", "Level 7 Cooler 2"], world.player) and state.has("Level 7 Bubble 9", world.player))
    set_rule(world.get_location("One Level 8"), lambda state: (state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or state.has("Level 8 Bubble 4", world.player))
    set_rule(world.get_location("One Level 9"), lambda state: state.has_any(["Level 9 Cooler 1", "Level 9 Cooler 2"], world.player))
    set_rule(world.get_location("One Level 10"), lambda state: state.has_any(["Level 10 Cooler 1", "Level 10 Cooler 3"], world.player) or state.has_all(["Level 10 Cooler 2", "Level 10 Bubble 9"], world.player))
    set_rule(world.get_location("One Level 11"), lambda state: True)
    set_rule(world.get_location("One Level 12"), lambda state: state.has_any(["Level 12 Cooler 1", "Level 12 Cooler 2"], world.player))
    set_rule(world.get_location("One Level 13"), lambda state: True)
    set_rule(world.get_location("One Level 14"), lambda state: state.has_all(["Level 14 Bubble 1", "Level 14 Cooler 2"], world.player) or state.has_all(["Level 14 Bubble " + str(bubble + 2) for bubble in range(6)] + ["Level 14 Cooler 1"], world.player))
    set_rule(world.get_location("One Level 15"), lambda state: state.has_any(["Level 15 Cooler 1", "Level 15 Cooler 2", "Level 15 Cooler 3"], world.player))


def set_completion_condition(world: SweetDefeatWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Level 5 Node", world.player)
