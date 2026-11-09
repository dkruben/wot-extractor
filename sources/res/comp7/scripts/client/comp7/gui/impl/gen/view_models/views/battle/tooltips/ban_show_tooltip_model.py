# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/battle/tooltips/ban_show_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/battle/tooltips/ban_show_tooltip_model.py
from frameworks.wulf import ViewModel

class BanShowTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(BanShowTooltipModel, self).__init__(properties=properties, commands=commands)

    def getLongName(self):
        return self._getString(0)

    def setLongName(self, value):
        self._setString(0, value)

    def getVehicleCD(self):
        return self._getNumber(1)

    def setVehicleCD(self, value):
        self._setNumber(1, value)

    def getType(self):
        return self._getString(2)

    def setType(self, value):
        self._setString(2, value)

    def getRoleKey(self):
        return self._getString(3)

    def setRoleKey(self, value):
        self._setString(3, value)

    def getIsPremium(self):
        return self._getBool(4)

    def setIsPremium(self, value):
        self._setBool(4, value)

    def getConfirmedChoice(self):
        return self._getBool(5)

    def setConfirmedChoice(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(BanShowTooltipModel, self)._initialize()
        self._addStringProperty('longName', '')
        self._addNumberProperty('vehicleCD', 0)
        self._addStringProperty('type', '')
        self._addStringProperty('roleKey', '')
        self._addBoolProperty('isPremium', False)
        self._addBoolProperty('confirmedChoice', False)
