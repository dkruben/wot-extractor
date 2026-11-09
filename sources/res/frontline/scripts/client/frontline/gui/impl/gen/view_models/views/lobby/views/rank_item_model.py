# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/rank_item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/rank_item_model.py
from frameworks.wulf import Array, ViewModel

class RankItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RankItemModel, self).__init__(properties=properties, commands=commands)

    def getRankName(self):
        return self._getString(0)

    def setRankName(self, value):
        self._setString(0, value)

    def getRankPoints(self):
        return self._getArray(1)

    def setRankPoints(self, value):
        self._setArray(1, value)

    @staticmethod
    def getRankPointsType():
        return int

    def _initialize(self):
        super(RankItemModel, self)._initialize()
        self._addStringProperty('rankName', '')
        self._addArrayProperty('rankPoints', Array())
