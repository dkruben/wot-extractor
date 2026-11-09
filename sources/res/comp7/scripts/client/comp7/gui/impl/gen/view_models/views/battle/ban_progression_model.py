# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/battle/ban_progression_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/battle/ban_progression_model.py
from comp7.gui.impl.gen.view_models.views.battle.enums import BanState
from frameworks.wulf import ViewModel

class BanProgressionModel(ViewModel):
    __slots__ = ('pollServerTime', )

    def __init__(self, properties=4, commands=1):
        super(BanProgressionModel, self).__init__(properties=properties, commands=commands)

    def getBanState(self):
        return BanState(self._getString(0))

    def setBanState(self, value):
        self._setString(0, value.value)

    def getStartTimestamp(self):
        return self._getNumber(1)

    def setStartTimestamp(self, value):
        self._setNumber(1, value)

    def getEndTimestamp(self):
        return self._getNumber(2)

    def setEndTimestamp(self, value):
        self._setNumber(2, value)

    def getServerTimestamp(self):
        return self._getNumber(3)

    def setServerTimestamp(self, value):
        self._setNumber(3, value)

    def _initialize(self):
        super(BanProgressionModel, self)._initialize()
        self._addStringProperty('banState')
        self._addNumberProperty('startTimestamp', 0)
        self._addNumberProperty('endTimestamp', 0)
        self._addNumberProperty('serverTimestamp', 0)
        self.pollServerTime = self._addCommand('pollServerTime')
