# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/post_battle_results_view/battle_financial_report_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/post_battle_results_view/battle_financial_report_model.py
from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.vehicle_financial_report_model import VehicleFinancialReportModel

class BattleFinancialReportModel(ViewModel):
    __slots__ = ()
    PLAYER_RANK_XP = 'playerRankXP'

    def __init__(self, properties=3, commands=0):
        super(BattleFinancialReportModel, self).__init__(properties=properties, commands=commands)

    def getHasAnyPremium(self):
        return self._getBool(0)

    def setHasAnyPremium(self, value):
        self._setBool(0, value)

    def getHasWotPlus(self):
        return self._getBool(1)

    def setHasWotPlus(self, value):
        self._setBool(1, value)

    def getVehiclesFinancialStats(self):
        return self._getArray(2)

    def setVehiclesFinancialStats(self, value):
        self._setArray(2, value)

    @staticmethod
    def getVehiclesFinancialStatsType():
        return VehicleFinancialReportModel

    def _initialize(self):
        super(BattleFinancialReportModel, self)._initialize()
        self._addBoolProperty('hasAnyPremium', False)
        self._addBoolProperty('hasWotPlus', False)
        self._addArrayProperty('vehiclesFinancialStats', Array())
