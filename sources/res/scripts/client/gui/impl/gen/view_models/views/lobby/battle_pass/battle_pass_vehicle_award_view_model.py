# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_vehicle_award_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/battle_pass_vehicle_award_view_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class BattlePassVehicleAwardViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(BattlePassVehicleAwardViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def vehicleInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getVehicleLevelPoints(self):
        return self._getNumber(1)

    def setVehicleLevelPoints(self, value):
        self._setNumber(1, value)

    def getBattlePassPointsAward(self):
        return self._getNumber(2)

    def setBattlePassPointsAward(self, value):
        self._setNumber(2, value)

    def getTechName(self):
        return self._getString(3)

    def setTechName(self, value):
        self._setString(3, value)

    def getIsPostProgression(self):
        return self._getBool(4)

    def setIsPostProgression(self, value):
        self._setBool(4, value)

    def getChapterID(self):
        return self._getNumber(5)

    def setChapterID(self, value):
        self._setNumber(5, value)

    def getIsBattlePassPurchased(self):
        return self._getBool(6)

    def setIsBattlePassPurchased(self, value):
        self._setBool(6, value)

    def _initialize(self):
        super(BattlePassVehicleAwardViewModel, self)._initialize()
        self._addViewModelProperty('vehicleInfo', VehicleInfoModel())
        self._addNumberProperty('vehicleLevelPoints', 0)
        self._addNumberProperty('battlePassPointsAward', 0)
        self._addStringProperty('techName', '')
        self._addBoolProperty('isPostProgression', False)
        self._addNumberProperty('chapterID', 0)
        self._addBoolProperty('isBattlePassPurchased', False)
