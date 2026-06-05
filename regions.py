from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import SweetDefeatWorld


def create_and_connect_regions(world: SweetDefeatWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: SweetDefeatWorld) -> None:
    world.multiworld.regions.append(Region("Game", world.player, world.multiworld))


def connect_regions(world: SweetDefeatWorld) -> None:
    pass
