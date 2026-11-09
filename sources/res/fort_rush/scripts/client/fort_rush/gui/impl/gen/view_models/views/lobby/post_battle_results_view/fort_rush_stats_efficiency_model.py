# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/lobby/post_battle_results_view/fort_rush_stats_efficiency_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/lobby/post_battle_results_view/fort_rush_stats_efficiency_model.py
from frameworks.wulf import ViewModel

class FortRushStatsEfficiencyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(FortRushStatsEfficiencyModel, self).__init__(properties=properties, commands=commands)

    def getFortRushScore(self):
        return self._getNumber(0)

    def setFortRushScore(self, value):
        self._setNumber(0, value)

    def getDamageDealt(self):
        return self._getNumber(1)

    def setDamageDealt(self, value):
        self._setNumber(1, value)

    def getKills(self):
        return self._getNumber(2)

    def setKills(self, value):
        self._setNumber(2, value)

    def getRespawns(self):
        return self._getNumber(3)

    def setRespawns(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(FortRushStatsEfficiencyModel, self)._initialize()
        self._addNumberProperty('fortRushScore', 0)
        self._addNumberProperty('damageDealt', 0)
        self._addNumberProperty('kills', 0)
        self._addNumberProperty('respawns', 0)
