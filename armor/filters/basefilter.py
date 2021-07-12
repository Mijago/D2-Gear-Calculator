
class BaseFilter:
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
