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


class Breathlink(Toggle):
    """
    Toggles breathlink for the player. Breathlink for Sweet Defeat is when the player's popsicle melts.
    """

    display_name = "Breathlink"
    default = False


@dataclass
class SweetDefeatOptions(PerGameCommonOptions):
    death_link: Deathlink
    death_link_amnesty: DeathlinkAmnesty
    breath_link: Breathlink


option_groups = []

option_presets = {}
