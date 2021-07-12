from armor.filters.basefilter import BaseFilter


class MaximalExoticFilter(BaseFilter):
    def apply(self, G, path, values, names):
        return values["exotic"] < 2
