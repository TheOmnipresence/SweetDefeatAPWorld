from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class Deathlink(Toggle):
    """
    Toggles deathlink for the player.
    """

    display_name = "Deathlink"
    default = False


class DeathlinkAmnesty(Range):
    """
    The amount of deaths required to send a deathlink.
    """

    display_name = "Deathlink Amnesty"
    range_start = 1
    range_end = 20
    default = 1

@dataclass
class SweetDefeatOptions(PerGameCommonOptions):
    death_link: Deathlink


option_groups = []

option_presets = {}
