from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


# For our game to display correctly on the website, we need to define a WebWorld subclass.
class SweetDefeatWebWorld(WebWorld):
    # We need to override the "game" field of the WebWorld superclass.
    # This must be the same string as the regular World class.
    game = "Sweet Defeat"

    # Your game pages will have a visual theme (affecting e.g. the background image).
    # You can choose between dirt, grass, grassFlowers, ice, jungle, ocean, partyTime, and stone.
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
