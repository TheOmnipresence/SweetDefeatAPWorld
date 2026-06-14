from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


class SweetDefeatWebWorld(WebWorld):
    game = "Sweet Defeat"

    theme = "grass"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Sweet Defeat for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["InterestedSC2"],
    )

    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets
