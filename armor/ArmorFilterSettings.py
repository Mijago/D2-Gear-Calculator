from armor.enums import Stat
from armor.filters.MaximalExoticFilter import MaximalExoticFilter
from armor.filters.basefilter import BaseFilter


class ArmorFilterSettings:
    def __init__(self):
        self.itemFilters = [
            MaximalExoticFilter()
        ]
        self.clazz = "Titan"
        self.weights = {
            Stat.Mobility.value: 1,
            Stat.Resilience.value: 1,
            Stat.Recovery.value: 1,
            Stat.Discipline.value: 1,
            Stat.Intellect.value: 1,
            Stat.Strength.value: 1,
        }

        self.staticStats = {
            Stat.Mobility.value: 0,
            Stat.Resilience.value: 0,
            Stat.Recovery.value: 0,
            Stat.Discipline.value: 0,
            Stat.Intellect.value: 0,
            Stat.Strength.value: 0,
        }
        self.wastedStatPenaltyWeight = {
            Stat.Mobility.value: 4,
            Stat.Resilience.value: 4,
            Stat.Recovery.value: 4,
            Stat.Discipline.value: 4,
            Stat.Intellect.value: 4,
            Stat.Strength.value: 4,
        }
        self.wastedStatPenaltyWeightOver100 = {
            Stat.Mobility.value: 1.1,
            Stat.Resilience.value: 1.1,
            Stat.Recovery.value: 1.1,
            Stat.Discipline.value: 1.1,
            Stat.Intellect.value: 1.1,
            Stat.Strength.value: 1.1,
        }

    def setClass(self, clazz):
        self.clazz = clazz
        return self

    def addStaticStat(self, stat, value):
        self.staticStats[stat.value] += value
        return self

    def setStatWeight(self, stat, weight):
        self.weights[stat.value] = weight
        return self

    def setWastedStatPenaltyWeight(self, stat, weight, over100):
        self.wastedStatPenaltyWeight[stat.value] = weight
        self.wastedStatPenaltyWeightOver100[stat.value] = over100
        return self

    def addFilter(self, filter: BaseFilter):
        self.itemFilters.append(filter)
        return self


class ExtendedArmorFilterSettings(ArmorFilterSettings):
    def __init__(self):
        super(ExtendedArmorFilterSettings, self).__init__()

    def addStaticPowerfulFriends(self):
        """Adds 20 mobility as static stats."""
        return self.addStaticStat(Stat.Mobility, 20)

    def addStaticRadiantLight(self):
        """Adds 20 strength as static stats."""
        return self.addStaticStat(Stat.Mobility, 20)

    def addStaticStasisWhisperOfChains(self):
        """Adds 10 recovery as static stats."""
        return self.addStaticStat(Stat.Recovery, 10)

    def addStaticStasisWhisperOfConduction(self):
        """Adds 10 resilience and 10 intellect as static stats."""
        self.addStaticStat(Stat.Resilience, 10)
        return self.addStaticStat(Stat.Intellect, 10)

    def addStaticStasisWhisperOfDurance(self):
        """Adds 10 strength as static stats."""
        return self.addStaticStat(Stat.Strength, 10)

    def addStaticStasisWhisperOfShards(self):
        """Adds 10 resilience as static stats."""
        return self.addStaticStat(Stat.Resilience, 10)
