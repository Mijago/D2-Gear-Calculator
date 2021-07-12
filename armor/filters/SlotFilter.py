from armor.filters.basefilter import BaseFilter


class SlotFilter(BaseFilter):
    def __init__(self, slot, name):
        self.slot = slot
        self.name = name

    def apply(self, G, indices, values, names):
        return names[self.slot.value] == self.name
