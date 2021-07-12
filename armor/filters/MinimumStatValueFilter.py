from armor.filters.basefilter import BaseFilter


class MinimumStatValueFilter(BaseFilter):
    def __init__(self, slot, minValue):
        self.slot = slot
        self.minValue = minValue

    def apply(self, G, indices, values, names):
        return values[self.slot.value] >= self.minValue


class MaximumStatValueFilter(BaseFilter):
    def __init__(self, stat, minValue):
        self.stat = stat
        self.minValue = minValue

    def apply(self, G, indices, values, names):
        return values[self.stat.value] <= self.minValue
