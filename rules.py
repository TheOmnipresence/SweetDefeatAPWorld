from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from .locations import LEVEL_TYPES, MAX_LEVELS

if TYPE_CHECKING:
    from .world import SweetDefeatWorld


def set_all_rules(world: SweetDefeatWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: SweetDefeatWorld) -> None:
    pass


def set_all_location_rules(world: SweetDefeatWorld) -> None:
    for i in ["Normal", "Invisible", "Pacifism"]:
        set_level_rule(world, i + " Level 1", lambda state: state.has("Level 1 Node", world.player))
        set_level_rule(world, i + " Level 2", lambda state: True)
        set_level_rule(world, i + " Level 3", lambda state: state.has_all(["Level 3 Cooler 1", "Level 3 Cooler 2", "Level 3 Cooler 3"], world.player))
        set_level_rule(world, i + " Level 4", lambda state: state.has_all(["Level 4 Bubble 1", "Level 4 Bubble 2", "Level 4 Bubble 3", "Level 4 Bubble 4"], world.player))
        set_level_rule(world, i + " Level 5", lambda state: state.has_all(["Level 5 Cooler 1", "Level 5 Cooler 2", "Level 5 Cooler 3", "Level 5 Cooler 4", "Level 5 Bubble 2", "Level 5 Bubble 3", "Level 5 Bubble 4"], world.player))
        set_level_rule(world, i + " Level 6", lambda state: (state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or (state.has("Level 6 Bubble 4", world.player) and world.options.hard_skips))
        set_level_rule(world, i + " Level 7", lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or (state.has("Level 7 Bubble 4", world.player) and world.options.hard_skips)) and state.has_all(["Level 7 Bubble 9", "Level 7 Cooler 1", "Level 7 Cooler 2"], world.player))
        set_level_rule(world, i + " Level 8", lambda state: ((state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or (state.has("Level 8 Bubble 4", world.player) and world.options.hard_skips)) and state.has_all(["Level 8 Bubble 9", "Level 8 Bubble 11"], world.player))
        set_level_rule(world, i + " Level 9", lambda state: state.has_any(["Level 9 Cooler 1", "Level 9 Cooler 2"], world.player))
        set_level_rule(world, i + " Level 10", lambda state: state.has_all(["Level 10 Cooler 1", "Level 10 Cooler 2", "Level 10 Cooler 3", "Level 10 Bubble 9", "Level 10 Bubble 11"], world.player))
        set_level_rule(world, i + " Level 11", lambda state: True)
        set_level_rule(world, i + " Level 12", lambda state: state.has_all(["Level 12 Cooler 1", "Level 12 Cooler 2"], world.player))
        set_level_rule(world, i + " Level 13", lambda state: True)
        set_level_rule(world, i + " Level 14", lambda state: (state.has_all(["Level 14 Bubble 1", "Level 14 Cooler 2"], world.player) and world.options.hard_skips) or state.has_all(["Level 14 Bubble " + str(bubble + 2) for bubble in range(6)] + ["Level 14 Cooler 1"], world.player))
        set_level_rule(world, i + " Level 15", lambda state: state.has_all(["Level 15 Cooler " + str(cooler + 1) for cooler in range(3)], world.player))
        set_level_rule(world, i + " Level 16", lambda state: state.has("Level 16 Cooler 1", world.player))
        set_level_rule(world, i + " Level 17", lambda state: True)
        set_level_rule(world, i + " Level 18", lambda state: state.has_all(["Level 18 Bubble 1", "Level 18 Bubble 2", "Level 18 Bubble 3"], world.player))
        set_level_rule(world, i + " Level 19", lambda state: True)
        set_level_rule(world, i + " Level 20", lambda state: True)
        set_level_rule(world, i + " Level 21", lambda state: state.has("Level 21 Cooler 1", world.player))
        set_level_rule(world, i + " Level 22", lambda state: state.has_all(["Level 22 Cooler 1", "Level 22 Cooler 2"], world.player))
        set_level_rule(world, i + " Level 23", lambda state: True)
        set_level_rule(world, i + " Level 24", lambda state: True)
        set_level_rule(world, i + " Level 25", lambda state: state.has_all(["Level 25 Cooler 1", "Level 25 Cooler 2", "Level 25 Cooler 3", "Level 25 Cooler 4"], world.player))
        set_level_rule(world, i + " Level 26", lambda state: state.has("Level 26 Cooler 1", world.player))
        set_level_rule(world, i + " Level 27", lambda state: True)
        set_level_rule(world, i + " Level 28", lambda state: state.has_all(["Level 28 Cooler 1", "Level 28 Cooler 2"], world.player))
        set_level_rule(world, i + " Level 29", lambda state: True)
        set_level_rule(world, i + " Level 30", lambda state: state.has("Level 30 Cooler 1", world.player))

    set_level_rule(world, "Node Level 1", lambda state: state.has("Level 1 Node", world.player))
    set_level_rule(world, "Node Level 2", lambda state: state.has("Level 2 Node", world.player))
    set_level_rule(world, "Node Level 3", lambda state: state.has("Level 3 Node", world.player))
    set_level_rule(world, "Node Level 4", lambda state: state.has("Level 4 Node", world.player))
    set_level_rule(world, "Node Level 5", lambda state: state.has_all(["Level 5 Node", "Level 5 Bubble 2", "Level 5 Bubble 3", "Level 5 Bubble 4"], world.player))
    set_level_rule(world, "Node Level 6", lambda state: ((state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or (state.has("Level 6 Bubble 4", world.player) and world.options.hard_skips)) and state.has("Level 6 Node", world.player))
    set_level_rule(world, "Node Level 7", lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or (state.has("Level 7 Bubble 4", world.player) and world.options.hard_skips)) and state.has_all(["Level 7 Bubble 9", "Level 7 Node"], world.player))
    set_level_rule(world, "Node Level 8", lambda state: ((state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or (state.has("Level 8 Bubble 4", world.player) and world.options.hard_skips)) and state.has_all(["Level 8 Bubble 9", "Level 8 Bubble 11", "Level 8 Node"], world.player))
    set_level_rule(world, "Node Level 9", lambda state: state.has("Level 9 Node", world.player))
    set_level_rule(world, "Node Level 10", lambda state: state.has("Level 10 Node", world.player))
    set_level_rule(world, "Node Level 11", lambda state: state.has("Level 11 Node", world.player))
    set_level_rule(world, "Node Level 12", lambda state: state.has("Level 12 Node", world.player))
    set_level_rule(world, "Node Level 13", lambda state: state.has("Level 13 Node", world.player))
    set_level_rule(world, "Node Level 14", lambda state: state.has("Level 14 Node", world.player))
    set_level_rule(world, "Node Level 15", lambda state: state.has("Level 15 Node", world.player))
    set_level_rule(world, "Node Level 16", lambda state: state.has("Level 16 Node", world.player))
    set_level_rule(world, "Node Level 17", lambda state: state.has("Level 17 Node", world.player))
    set_level_rule(world, "Node Level 18", lambda state: state.has("Level 18 Node", world.player))
    set_level_rule(world, "Node Level 19", lambda state: state.has("Level 19 Node", world.player))
    set_level_rule(world, "Node Level 20", lambda state: state.has("Level 20 Node", world.player))
    set_level_rule(world, "Node Level 21", lambda state: state.has("Level 21 Node", world.player))
    set_level_rule(world, "Node Level 22", lambda state: state.has("Level 22 Node", world.player))
    set_level_rule(world, "Node Level 23", lambda state: state.has("Level 23 Node", world.player))
    set_level_rule(world, "Node Level 24", lambda state: state.has("Level 24 Node", world.player))
    set_level_rule(world, "Node Level 25", lambda state: state.has("Level 25 Node", world.player))
    set_level_rule(world, "Node Level 26", lambda state: state.has("Level 26 Node", world.player))
    set_level_rule(world, "Node Level 27", lambda state: state.has("Level 27 Node", world.player))
    set_level_rule(world, "Node Level 28", lambda state: state.has_all(["Level 28 Node", "Level 28 Cooler 1"], world.player))
    set_level_rule(world, "Node Level 29", lambda state: state.has("Level 29 Node", world.player))
    set_level_rule(world, "Node Level 30", lambda state: state.has_all(["Level 30 Node", "Level 30 Cooler 1"], world.player))

    set_level_rule(world, "Rampage Level 1", lambda state: True)
    set_level_rule(world, "Rampage Level 2", lambda state: True)
    set_level_rule(world, "Rampage Level 3", lambda state: True)
    set_level_rule(world, "Rampage Level 4", lambda state: True)
    set_level_rule(world, "Rampage Level 5", lambda state: True)
    set_level_rule(world, "Rampage Level 6", lambda state: (state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or (state.has("Level 6 Bubble 4", world.player) and world.options.hard_skips))
    set_level_rule(world, "Rampage Level 7", lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or (state.has("Level 7 Bubble 4", world.player) and world.options.hard_skips)) and state.has("Level 7 Bubble 9", world.player))
    set_level_rule(world, "Rampage Level 8", lambda state: ((state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or (state.has("Level 8 Bubble 4", world.player) and world.options.hard_skips)) and state.has_all(["Level 8 Bubble 9", "Level 8 Bubble 11"], world.player))
    set_level_rule(world, "Rampage Level 9", lambda state: state.has_any(["Level 9 Cooler 1", "Level 9 Cooler 2", "Level 9 Bubble 9"], world.player) and state.has("Level 9 Bubble 11", world.player))
    set_level_rule(world, "Rampage Level 10", lambda state: state.has("Level 10 Cooler 1", world.player))
    set_level_rule(world, "Rampage Level 11", lambda state: True)
    set_level_rule(world, "Rampage Level 12", lambda state: True)
    set_level_rule(world, "Rampage Level 13", lambda state: True)
    set_level_rule(world, "Rampage Level 14", lambda state: True)
    set_level_rule(world, "Rampage Level 15", lambda state: True)
    set_level_rule(world, "Rampage Level 16", lambda state: True)
    set_level_rule(world, "Rampage Level 17", lambda state: True)
    set_level_rule(world, "Rampage Level 18", lambda state: True)
    set_level_rule(world, "Rampage Level 19", lambda state: True)
    set_level_rule(world, "Rampage Level 20", lambda state: True)
    set_level_rule(world, "Rampage Level 21", lambda state: True)
    set_level_rule(world, "Rampage Level 22", lambda state: True)
    set_level_rule(world, "Rampage Level 23", lambda state: True)
    set_level_rule(world, "Rampage Level 24", lambda state: True)
    set_level_rule(world, "Rampage Level 25", lambda state: True)
    set_level_rule(world, "Rampage Level 26", lambda state: True)
    set_level_rule(world, "Rampage Level 27", lambda state: True)
    set_level_rule(world, "Rampage Level 28", lambda state: state.has_all(["Level 28 Cooler 1", "Level 28 Cooler 2"], world.player))
    set_level_rule(world, "Rampage Level 29", lambda state: state.has("Level 29 Cooler 1", world.player))
    set_level_rule(world, "Rampage Level 30", lambda state: state.has("Level 30 Cooler 1", world.player))

    set_level_rule(world, "Cool Level 1", lambda state: state.has("Level 1 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 2", lambda state: state.has("Level 2 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 3", lambda state: state.has_all(["Level 3 Cooler 1", "Level 3 Cooler 2", "Level 3 Cooler 3"], world.player))
    set_level_rule(world, "Cool Level 4", lambda state: state.has_all(["Level 4 Cooler 1", "Level 4 Cooler 2", "Level 4 Cooler 3"], world.player))
    set_level_rule(world, "Cool Level 5", lambda state: state.has_all(["Level 5 Cooler 1", "Level 5 Cooler 2", "Level 5 Cooler 3", "Level 5 Cooler 4", "Level 5 Bubble 3", "Level 5 Bubble 4"], world.player))
    set_level_rule(world, "Cool Level 6", lambda state: ((state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or (state.has("Level 6 Bubble 4", world.player) and world.options.hard_skips)) and state.has("Level 6 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 7", lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or (state.has("Level 7 Bubble 4", world.player) and world.options.hard_skips)) and state.has_all(["Level 7 Bubble 9", "Level 7 Cooler 1", "Level 7 Cooler 2"], world.player))
    set_level_rule(world, "Cool Level 8", lambda state: ((state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or (state.has("Level 8 Bubble 4", world.player) and world.options.hard_skips)) and state.has_all(["Level 8 Bubble 9", "Level 8 Cooler 1", "Level 8 Cooler 2"], world.player))
    set_level_rule(world, "Cool Level 9", lambda state: state.has_all(["Level 9 Cooler 1", "Level 9 Cooler 2"], world.player))
    set_level_rule(world, "Cool Level 10", lambda state: state.has_all(["Level 10 Cooler 1", "Level 10 Cooler 2", "Level 10 Cooler 3", "Level 10 Bubble 9"], world.player))
    set_level_rule(world, "Cool Level 11", lambda state: state.has("Level 11 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 12", lambda state: state.has_all(["Level 12 Cooler 1", "Level 12 Cooler 2"], world.player))
    set_level_rule(world, "Cool Level 13", lambda state: state.has_all(["Level 13 Cooler 1", "Level 13 Cooler 2"], world.player))
    set_level_rule(world, "Cool Level 14", lambda state: state.has_all(["Level 14 Cooler 1", "Level 14 Cooler 2"], world.player))
    set_level_rule(world, "Cool Level 15", lambda state: state.has_all(["Level 15 Cooler 1", "Level 15 Cooler 2", "Level 15 Cooler 3"], world.player))
    set_level_rule(world, "Cool Level 16", lambda state: state.has("Level 16 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 17", lambda state: state.has("Level 17 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 18", lambda state: state.has("Level 18 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 19", lambda state: state.has("Level 19 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 20", lambda state: state.has("Level 20 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 21", lambda state: state.has("Level 21 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 22", lambda state: state.has_all(["Level 22 Cooler 1", "Level 22 Cooler 2"], world.player))
    set_level_rule(world, "Cool Level 23", lambda state: state.has_all(["Level 23 Cooler 1", "Level 23 Cooler 2", "Level 23 Cooler 3"], world.player))
    set_level_rule(world, "Cool Level 24", lambda state: state.has_all(["Level 24 Cooler 1", "Level 24 Cooler 2", "Level 24 Cooler 3", "Level 24 Cooler 4"], world.player))
    set_level_rule(world, "Cool Level 25", lambda state: state.has_all(["Level 25 Cooler 1", "Level 25 Cooler 2", "Level 25 Cooler 3", "Level 25 Cooler 4"], world.player))
    set_level_rule(world, "Cool Level 26", lambda state: state.has("Level 26 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 27", lambda state: state.has("Level 27 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 28", lambda state: state.has_all(["Level 28 Cooler 1", "Level 28 Cooler 2"], world.player))
    set_level_rule(world, "Cool Level 29", lambda state: state.has("Level 29 Cooler 1", world.player))
    set_level_rule(world, "Cool Level 30", lambda state: state.has("Level 30 Cooler 1", world.player))

    for i in range(30):
        set_level_rule(world, "Void Level " + str(i + 1), lambda state: True)

    set_level_rule(world, "Easier Level 1", lambda state: state.has("Level 1 Node", world.player))
    set_level_rule(world, "Easier Level 2", lambda state: True)
    set_level_rule(world, "Easier Level 3", lambda state: state.has_from_list_unique(["Level 3 Cooler 1", "Level 3 Cooler 2", "Level 3 Cooler 3"], world.player, 2))
    set_level_rule(world, "Easier Level 4", lambda state: state.has_from_list_unique(["Level 4 Bubble 1", "Level 4 Bubble 2", "Level 4 Bubble 3", "Level 4 Bubble 4"], world.player, 2))
    set_level_rule(world, "Easier Level 5", lambda state: state.has_from_list_unique(["Level 5 Bubble 1", "Level 5 Bubble 2", "Level 5 Bubble 3", "Level 5 Bubble 4"], world.player, 3) and state.has_from_list_unique(["Level 5 Cooler 1", "Level 5 Cooler 2", "Level 5 Cooler 3"], world.player, 2) and state.has("Level 5 Bubble 2", world.player)) #TODO TODO
    set_level_rule(world, "Easier Level 6", lambda state: (state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or (state.has("Level 6 Bubble 4", world.player) and world.options.hard_skips))
    set_level_rule(world, "Easier Level 7", lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or (state.has("Level 7 Bubble 4", world.player) and world.options.hard_skips)) and state.has("Level 7 Bubble 9", world.player) and state.has_any(["Level 7 Cooler 1", "Level 7 Cooler 2"], world.player))
    set_level_rule(world, "Easier Level 8", lambda state: ((state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or (state.has("Level 8 Bubble 4", world.player) and world.options.hard_skips)) and state.has("Level 8 Bubble 9", world.player))
    set_level_rule(world, "Easier Level 9", lambda state: state.has_any(["Level 9 Cooler 1", "Level 9 Cooler 2"], world.player))
    set_level_rule(world, "Easier Level 10", lambda state: (state.has_all(["Level 10 Cooler 1", "Level 10 Cooler 3"], world.player) or state.has_all(["Level 10 Cooler 1", "Level 10 Cooler 2", "Level 10 Bubble 9"], world.player) or state.has_all(["Level 10 Cooler 3", "Level 10 Cooler 2", "Level 10 Bubble 9"], world.player)) and state.has_from_list_unique(["Level 10 Bubble " + str(bubble + 1) for bubble in range(11)], world.player, 3))
    set_level_rule(world, "Easier Level 11", lambda state: True)
    set_level_rule(world, "Easier Level 12", lambda state: state.has_any(["Level 12 Cooler 1", "Level 12 Cooler 2"], world.player))
    set_level_rule(world, "Easier Level 13", lambda state: state.has_any(["Level 13 Cooler 1", "Level 13 Cooler 2"], world.player))
    set_level_rule(world, "Easier Level 14", lambda state: state.has_all(["Level 14 Bubble 1", "Level 14 Cooler 2"], world.player) or state.has_all(["Level 14 Bubble 2", "Level 14 Cooler 1"], world.player))
    set_level_rule(world, "Easier Level 15", lambda state: state.has_from_list_unique(["Level 15 Cooler " + str(cooler + 1) for cooler in range(3)], world.player, 2) and state.has_from_list_unique(["Level 15 Bubble " + str(cooler + 1) for cooler in range(7)], world.player, 2))
    set_level_rule(world, "Easier Level 16", lambda state: True)
    set_level_rule(world, "Easier Level 17", lambda state: state.has("Level 17 Cooler 1", world.player))
    set_level_rule(world, "Easier Level 18", lambda state: state.has_from_list_unique(["Level 18 Bubble " + str(bubble + 1) for bubble in range(3)], world.player, 2))
    set_level_rule(world, "Easier Level 19", lambda state: True)
    set_level_rule(world, "Easier Level 20", lambda state: True)
    set_level_rule(world, "Easier Level 21", lambda state: state.has("Level 21 Cooler 1", world.player))
    set_level_rule(world, "Easier Level 22", lambda state: state.has_any(["Level 22 Cooler 1", "Level 22 Cooler 2"], world.player))
    set_level_rule(world, "Easier Level 23", lambda state: True)
    set_level_rule(world, "Easier Level 24", lambda state: state.has_from_list_unique(["Level 24 Cooler 1", "Level 24 Cooler 2", "Level 24 Cooler 3", "Level 24 Cooler 4"], world.player, 2))
    set_level_rule(world, "Easier Level 25", lambda state: state.has_from_list_unique(["Level 25 Cooler 1", "Level 25 Cooler 2", "Level 25 Cooler 3", "Level 25 Cooler 4"], world.player, 2))
    set_level_rule(world, "Easier Level 26", lambda state: True)
    set_level_rule(world, "Easier Level 27", lambda state: state.has("Level 27 Cooler 1", world.player))
    set_level_rule(world, "Easier Level 28", lambda state: state.has("Level 28 Cooler 1", world.player))
    set_level_rule(world, "Easier Level 29", lambda state: True)
    set_level_rule(world, "Easier Level 30", lambda state: state.has("Level 30 Cooler 1", world.player))

    set_level_rule(world, "One Level 1", lambda state: state.has("Level 1 Node", world.player))
    set_level_rule(world, "One Level 2", lambda state: True)
    set_level_rule(world, "One Level 3", lambda state: state.has_any(["Level 3 Cooler 1", "Level 3 Cooler 2", "Level 3 Cooler 3"], world.player))
    set_level_rule(world, "One Level 4", lambda state: state.has_any(["Level 4 Bubble 1", "Level 4 Bubble 2", "Level 4 Bubble 3", "Level 4 Bubble 4"], world.player))
    set_level_rule(world, "One Level 5", lambda state: state.has_any(["Level 5 Cooler 1", "Level 5 Cooler 2", "Level 5 Cooler 3"], world.player) or state.has_all(["Level 5 Bubble 2", "Level 5 Bubble 3", "Level 5 Bubble 4", "Level 5 Cooler 4"], world.player))
    set_level_rule(world, "One Level 6", lambda state: (state.has("Level 6 Bubble 5", world.player) and (state.has("Level 6 Bubble 4", world.player) or state.has("Level 6 Bubble 3", world.player))) or (state.has("Level 6 Bubble 4", world.player) and world.options.hard_skips))
    set_level_rule(world, "One Level 7", lambda state: ((state.has("Level 7 Bubble 5", world.player) and (state.has("Level 7 Bubble 4", world.player) or state.has("Level 7 Bubble 3", world.player))) or (state.has("Level 7 Bubble 4", world.player) and world.options.hard_skips)) and state.has_any(["Level 7 Cooler 1", "Level 7 Cooler 2"], world.player) and state.has("Level 7 Bubble 9", world.player))
    set_level_rule(world, "One Level 8", lambda state: (state.has("Level 8 Bubble 5", world.player) and (state.has("Level 8 Bubble 4", world.player) or state.has("Level 8 Bubble 3", world.player))) or (state.has("Level 8 Bubble 4", world.player) and world.options.hard_skips))
    set_level_rule(world, "One Level 9", lambda state: state.has_any(["Level 9 Cooler 1", "Level 9 Cooler 2"], world.player))
    set_level_rule(world, "One Level 10", lambda state: state.has_any(["Level 10 Cooler 1", "Level 10 Cooler 3"], world.player) or state.has_all(["Level 10 Cooler 2", "Level 10 Bubble 9"], world.player))
    set_level_rule(world, "One Level 11", lambda state: True)
    set_level_rule(world, "One Level 12", lambda state: state.has_any(["Level 12 Cooler 1", "Level 12 Cooler 2"], world.player))
    set_level_rule(world, "One Level 13", lambda state: True)
    set_level_rule(world, "One Level 14", lambda state: state.has_all(["Level 14 Bubble 1", "Level 14 Cooler 2"], world.player) or state.has_all(["Level 14 Bubble " + str(bubble + 2) for bubble in range(6)] + ["Level 14 Cooler 1"], world.player))
    set_level_rule(world, "One Level 15", lambda state: state.has_any(["Level 15 Cooler 1", "Level 15 Cooler 2", "Level 15 Cooler 3"], world.player))
    set_level_rule(world, "One Level 16", lambda state: state.has("Level 16 Cooler 1", world.player))
    set_level_rule(world, "One Level 17", lambda state: True)
    set_level_rule(world, "One Level 18", lambda state: state.has_any(["Level 18 Bubble " + str(bubble + 1) for bubble in range(3)], world.player))
    set_level_rule(world, "One Level 19", lambda state: True)
    set_level_rule(world, "One Level 20", lambda state: True)
    set_level_rule(world, "One Level 21", lambda state: state.has("Level 21 Cooler 1", world.player))
    set_level_rule(world, "One Level 22", lambda state: state.has_any(["Level 22 Cooler 1", "Level 22 Cooler 2"], world.player))
    set_level_rule(world, "One Level 23", lambda state: True)
    set_level_rule(world, "One Level 24", lambda state: True)
    set_level_rule(world, "One Level 25", lambda state: state.has_any(["Level 25 Cooler 1", "Level 25 Cooler 2", "Level 25 Cooler 3", "Level 25 Cooler 4"], world.player))
    set_level_rule(world, "One Level 26", lambda state: state.has("Level 26 Cooler 1", world.player))
    set_level_rule(world, "One Level 27", lambda state: True)
    set_level_rule(world, "One Level 28", lambda state: state.has("Level 28 Cooler 1", world.player))
    set_level_rule(world, "One Level 29", lambda state: True)
    set_level_rule(world, "One Level 30", lambda state: state.has("Level 30 Cooler 1", world.player))


def set_level_rule(world: SweetDefeatWorld, level: str, rule: Callable) -> None:
    if world.options.exclude_level_type.value - 1 == LEVEL_TYPES.index(level.split(" ")[0]):
        return
    set_rule(world.get_location(level), rule)


def set_completion_condition(world: SweetDefeatWorld) -> None:
    # 19 + 2 + 21 + 21 + 14 = 77 winds, only 37 spaces available, use H&S? it would add 50 checks.
    world.multiworld.completion_condition[world.player] = lambda state: can_goal(state, world)


def can_goal(state: CollectionState, world: SweetDefeatWorld) -> bool:
    if not state.has_all(["Level 31 Cooler 16", "Level 31 Bubble 3", "Level 31 Bubble 4", "Level 31 Bubble 14", "Level 31 Bubble 15"], world.player):
        return False
    for level in range(MAX_LEVELS):
        if not can_compete_level(level + 1, state, world):
            return False
    return True


def can_compete_level(level: int, state: CollectionState, world: SweetDefeatWorld) -> bool:
    for i in LEVEL_TYPES:
        if world.options.exclude_level_type.value - 1 == LEVEL_TYPES.index(i):
            continue
        if world.get_location(i + " Level " + str(level)).access_rule(state):
            return True
    return False
