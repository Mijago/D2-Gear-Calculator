from armor.ArmorFilter import ArmorFilter, Stat
from armor.ArmorFilterSettings import ExtendedArmorFilterSettings
from armor.enums import Slot
from armor.filters.SlotFilter import SlotFilter
from armor.filters.MinimumStatValueFilter import MaximumStatValueFilter, MinimumStatValueFilter

af = ArmorFilter(
    ExtendedArmorFilterSettings()
        # Prepare Settings
        .setClass("Hunter")
        .setStatWeight(Stat.Mobility, 1.5)
        .setStatWeight(Stat.Resilience, 0.5)
        .setStatWeight(Stat.Recovery, 1.5)
        .setStatWeight(Stat.Discipline, 0.5)
        .setStatWeight(Stat.Intellect, 0.6)
        .setStatWeight(Stat.Strength, 0.3)
        # You can also modify the penalty weights
        .setWastedStatPenaltyWeight(Stat.Mobility, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Resilience, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Recovery, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Discipline, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Intellect, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Strength, weight=4, over100=1.1)
        ## add base mods; you can also add stasis here manually, or use the shortcuts below
        # .addStaticStat(Stat.Mobility, 20)     # Powerful Friends
        # .addStaticStat(Stat.Strength, 20)     # Radiant Light
        ## As a shortcut, you can also use the following commands
        # .addStaticPowerfulFriends()           # +20 mobility
        # .addStaticRadiantLight()              # +20 strength
        ## STASIS
        # .addStaticStasisWhisperOfChains()     # +10 recovery
        # .addStaticStasisWhisperOfConduction() # +10 resilience, +10 intellect
        # .addStaticStasisWhisperOfDurance()    # +10 strength
        # .addStaticStasisWhisperOfShards()     # +10 resilience

        # Add filters
        # .addFilter(MinimumStatValueFilter(Stat.Mobility, 70)) # Mobility MUST be >= 70
        # .addFilter(MaximumStatValueFilter(Stat.Mobility, 80)) # Mobility MUST be <= 80
        # .addFilter(SlotFilter(Slot.Legs, "Dunemarchers"))     # Only builds with dunemarchers in the leg slot
)
af.buildGraphForFile("./destinyArmor.csv")
af.buildPaths()
af.getScores()
af.saveScored("./output.txt", num=100)
