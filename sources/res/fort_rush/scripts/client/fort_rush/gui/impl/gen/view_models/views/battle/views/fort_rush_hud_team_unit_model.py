# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/battle/views/fort_rush_hud_team_unit_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/views/battle/views/fort_rush_hud_team_unit_model.py
from gui.impl.gen.view_models.common.battle_player import VehicleTypeEnum
from frameworks.wulf import ViewModel

class FortRushHudTeamUnitModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(FortRushHudTeamUnitModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getType(self):
        return VehicleTypeEnum(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)

    def getIsDestroyed(self):
        return self._getBool(2)

    def setIsDestroyed(self, value):
        self._setBool(2, value)

    def _initialize(self):
        super(FortRushHudTeamUnitModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addStringProperty('type', VehicleTypeEnum.UNDEFINED.value)
        self._addBoolProperty('isDestroyed', False)
