# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tooltips/last_update_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tooltips/last_update_tooltip_model.py
from frameworks.wulf import ViewModel

class LastUpdateTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LastUpdateTooltipModel, self).__init__(properties=properties, commands=commands)

    def getLeaderboardUpdateTimestamp(self):
        return self._getNumber(0)

    def setLeaderboardUpdateTimestamp(self, value):
        self._setNumber(0, value)

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)

    def _initialize(self):
        super(LastUpdateTooltipModel, self)._initialize()
        self._addNumberProperty('leaderboardUpdateTimestamp', 0)
        self._addStringProperty('description', '')
