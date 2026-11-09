# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineBattleStatisticDataControllerMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/meta/FrontlineBattleStatisticDataControllerMeta.py
from gui.Scaleform.daapi.view.battle.shared.stats_exchange.stats_ctrl import BattleStatisticsDataController

class FrontlineBattleStatisticDataControllerMeta(BattleStatisticsDataController):

    def as_updateEpicPlayerStatsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEpicPlayerStats(data)

    def as_setEpicVehiclesStatsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setEpicVehiclesStats(data)

    def as_updateEpicVehiclesStatsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEpicVehiclesStats(data)
