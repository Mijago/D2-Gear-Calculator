from armor.filters.basefilter import BaseFilter


class MaximalExoticFilter(BaseFilter):
    filterName = "Exotic Limiter"
    filterDescription = "Only one exotic item is allowed per build."

    def apply(self, G, path, values, names):
        return values["exotic"] < 2
