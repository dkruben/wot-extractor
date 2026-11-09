# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/goodies/GoodieResources.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/goodies/GoodieResources.py
from __future__ import absolute_import
from typing import TYPE_CHECKING, TypeVar
from goodies.GoodieValue import GoodieValue
if TYPE_CHECKING:
    from typing import Generator

class GoodieResource(object):
    __slots__ = ('_value', )

    def __init__(self, value):
        self._value = value

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self._value == other._value

    def __hash__(self):
        return hash(self._value)

    def __repr__(self):
        return ('<{} value={}>').format(self.__class__.__name__, self._value)

    @property
    def value(self):
        return self._value

    @classmethod
    def provideCompatibleValueDescr(cls, actualVal, isPercent):
        if isPercent:
            return GoodieValue.percent(actualVal)
        return GoodieValue.absolute(actualVal)

    def iterate(self):
        yield self


class Gold(GoodieResource):

    def __init__(self, value):
        super(Gold, self).__init__(value)


class Credits(GoodieResource):

    def __init__(self, value):
        super(Credits, self).__init__(value)


class Experience(GoodieResource):

    def __init__(self, value):
        super(Experience, self).__init__(value)


class CrewExperience(GoodieResource):

    def __init__(self, value):
        super(CrewExperience, self).__init__(value)


class FreeExperience(GoodieResource):

    def __init__(self, value):
        super(FreeExperience, self).__init__(value)


class FrontlineExperience(GoodieResource):

    def __init__(self, value):
        super(FrontlineExperience, self).__init__(value)


GoodieResourceType = TypeVar('GoodieResourceType', bound=GoodieResource)
