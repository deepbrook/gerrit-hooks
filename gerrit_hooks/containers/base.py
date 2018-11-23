"""Container class for the gerrit-hooks library.

Supplies containers which store supported hooks, as well as flag definitions.
"""
from collections import Mapping


class Container(Mapping):
    __all__ = []

    def __iter__(self):
        return iter(self.__all__)

    def __getitem__(self, item):
        try:
            return getattr(self, item)
        except AttributeError:
            raise KeyError(item)

    def __len__(self):
        return len(self.__all__)

    def __contains__(self, item):
        return item in self.__all__
