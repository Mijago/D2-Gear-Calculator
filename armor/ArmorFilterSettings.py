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

    def setClass(self, clazz):
        self.clazz = clazz
        return self

    def addStaticStat(self, stat, value):
        self.staticStats[stat.value] += value
        return self

    def setStatWeight(self, stat, weight):
        self.weights[stat.value] = weight
        return self

    def addFilter(self, filter: BaseFilter):
        self.itemFilters.append(filter)
        return self