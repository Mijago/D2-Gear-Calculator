class BaseFilter:
    filterName = "BaseFilter"
    filterDescription = "Basic filter that doesn't do anything."

    def apply(self, G, path, values, names) -> bool:
        """
        Returns false if this path is not valid due to this filter
        :param G:
        :param path:
        :param values:
        :param names:
        :return:
        """
        pass

    def __str__(self) -> str:
        return self.filterName + ': ' + self.filterDescription
