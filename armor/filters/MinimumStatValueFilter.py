from armor.filters.basefilter import BaseFilter


class MinimumStatValueFilter(BaseFilter):
    filterName = "Stat Minimum"
    filterDescription = ""

    def __init__(self, stat, minValue):
        self.stat = stat
        self.minValue = minValue

        self.filterDescription = "{:s} must be at least {:d}.".format(stat.name, minValue)

    def apply(self, G, indices, values, names):
        return values[self.stat.value] >= self.minValue


class MaximumStatValueFilter(BaseFilter):
    filterName = "Stat Maximum"
    def __init__(self, stat, minValue):
        self.stat = stat
        self.minValue = minValue

        self.filterDescription = "{:s} must be lower than or equal to {:d}.".format(stat.name, minValue)

    def apply(self, G, indices, values, names):
        return values[self.stat.value] <= self.minValue
