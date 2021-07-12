from armor.ArmorFilter import ArmorFilter, Stat
from armor.ArmorFilterSettings import ArmorFilterSettings

af = ArmorFilter(
    ArmorFilterSettings()
        # Prepare Settings
        .setClass("Titan")
        .setStatWeight(Stat.Mobility, 0.3)
        .setStatWeight(Stat.Resilience, 1.5)
        .setStatWeight(Stat.Recovery, 1.2)
        .setStatWeight(Stat.Discipline, 1.5)
        .setStatWeight(Stat.Intellect, 0.6)
        .setStatWeight(Stat.Strength, 0.3)
        # You can also modify the penalty weights
        .setWastedStatPenaltyWeight(Stat.Mobility, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Resilience, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Recovery, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Discipline, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Intellect, weight=4, over100=1.1)
        .setWastedStatPenaltyWeight(Stat.Strength, weight=4, over100=1.1)
        # add base mods; you can also add stasis here
        .addStaticStat(Stat.Mobility, 20)  # Powerful Friends
        .addStaticStat(Stat.Strength, 20)  # Radiant Light
    # Add filters
    # .addFilter(MinimumStatValueFilter(Stat.Mobility, 18))
    # .addFilter(MaximumStatValueFilter(Stat.Mobility, 20))
    # .addFilter(SlotFilter(Slot.Legs, "Dunemarchers"))  # Only builds with dunemarchers
)
af.buildGraphForFile("./destinyArmor.csv")
af.buildPaths()
af.getScores()
af.saveScored("./output.txt", num=100)
