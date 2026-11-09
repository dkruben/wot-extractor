# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/goodies/GoodieConditions.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/goodies/GoodieConditions.py
from __future__ import absolute_import
from typing import TypeVar

class Condition(object):

    def check(self, other):
        return self == other

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    __hash__ = None


class MaxVehicleLevel(Condition):

    def __init__(self, level):
        self.level = level

    def __lt__(self, other):
        return self.level < other.level


GoodieConditionType = TypeVar('GoodieConditionType', bound=Condition)
