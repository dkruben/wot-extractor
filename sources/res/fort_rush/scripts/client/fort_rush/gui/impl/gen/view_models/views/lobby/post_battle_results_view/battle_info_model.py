# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/lobby/post_battle_results_view/battle_info_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/lobby/post_battle_results_view/battle_info_model.py
from frameworks.wulf import ViewModel

class BattleInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(BattleInfoModel, self).__init__(properties=properties, commands=commands)

    def getArenaName(self):
        return self._getString(0)

    def setArenaName(self, value):
        self._setString(0, value)

    def getBattleStartTime(self):
        return self._getNumber(1)

    def setBattleStartTime(self, value):
        self._setNumber(1, value)

    def getBattleDuration(self):
        return self._getNumber(2)

    def setBattleDuration(self, value):
        self._setNumber(2, value)

    def getWinStatus(self):
        return self._getString(3)

    def setWinStatus(self, value):
        self._setString(3, value)

    def getFinishReason(self):
        return self._getString(4)

    def setFinishReason(self, value):
        self._setString(4, value)

    def getFinishReasonClarification(self):
        return self._getString(5)

    def setFinishReasonClarification(self, value):
        self._setString(5, value)

    def _initialize(self):
        super(BattleInfoModel, self)._initialize()
        self._addStringProperty('arenaName', '')
        self._addNumberProperty('battleStartTime', 0)
        self._addNumberProperty('battleDuration', 0)
        self._addStringProperty('winStatus', '')
        self._addStringProperty('finishReason', '')
        self._addStringProperty('finishReasonClarification', '')
