from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, FreeText, OptionSet

from .locations import LEVEL_TYPES


def get_level_types_string() -> str:
    result = ""
    for i in LEVEL_TYPES:
        if i == LEVEL_TYPES[-1]:
            result += ", or " + i
        elif i == LEVEL_TYPES[0]:
            result += i
        else:
            result += ", " + i
    return result


class Deathlink(Toggle):
    """
    Toggles deathlink for the player.
    """

    display_name = "DeathLink"
    default = False


class DeathlinkAmnesty(Range):
    """
    The amount of deaths required to send a deathlink.
    """

    display_name = "DeathLink Amnesty"
    range_start = 1
    range_end = 20
    default = 1


class Breathlink(Toggle):
    """
    Toggles breathlink for the player. Breathlink for Sweet Defeat is when the player's popsicle melts.
    """

    display_name = "BreathLink"
    default = False


class DamageLink(Toggle):
    """
    Toggles damagelink for the player. 100 damagelink points is one health.
    """

    display_name = "DamageLink"
    default = False


class KnockbackLink(Toggle):
    """
    Toggles knockbacklink for the player. 1 knockbacklink point is 100 units of in-game speed (pixels).
    """

    display_name = "KnockbackLink"
    default = False


class KnockbackLinkSources(OptionSet):
    """
    The sources that the player should send a knockback link from.
    Acceptable values in this set are:
    - Any (all sources)
    - Bubbles
    - Lasers
    """

    display_name = "KnockbackLink Sources"
    default = ["Any"]


class ExcludeLevelType(Choice):
    """
    Excludes one level type.
    """

    display_name = "Exclude Level Type"
    option_none = 0
    option_exclude_normal = 1
    option_exclude_node = 2
    option_exclude_rampage = 3
    option_exclude_cool = 4
    option_exclude_invisible = 5
    option_exclude_pacifism = 6
    option_exclude_void = 7
    option_exclude_easier = 8
    option_exclude_one = 9
    default = 0


class HardSkips(Toggle):
    """
    If hard skips should be included in logic.
    """

    display_name = "Hard Skips"
    default = False


@dataclass
class SweetDefeatOptions(PerGameCommonOptions):
    death_link: Deathlink
    death_link_amnesty: DeathlinkAmnesty
    breath_link: Breathlink
    damage_link: DamageLink
    knockback_link: KnockbackLink
    knockback_link_sources: KnockbackLinkSources
    exclude_level_type: ExcludeLevelType
    hard_skips: HardSkips


option_groups = []

option_presets = {}
