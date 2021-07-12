from enum import Enum


class Slot(Enum):
    Helmet = "Helmet"
    Gauntlet = "Gauntlets"
    Chest = "Chest Armor"
    Legs = "Leg Armor"


class Stat(Enum):
    Mobility = "Mobility"
    Resilience = "Resilience"
    Recovery = "Recovery"
    Discipline = "Discipline"
    Intellect = "Intellect"
    Strength = "Strength"