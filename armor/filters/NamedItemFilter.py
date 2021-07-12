from armor.filters.basefilter import BaseFilter


class NamedItemFilter(BaseFilter):
    filterName = "Named Item Filter"

    def __init__(self, slot, name):
        self.slot = slot
        self.name = name

        self.filterDescription = "{:s} must have the name '{:s}'.".format(slot.name, name)

    def apply(self, G, indices, values, names):
        return names[self.slot.value] == self.name
