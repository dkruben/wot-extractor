# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/loot_box_compensation_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/loot_box_compensation_tooltip_model.py
from frameworks.wulf import ViewModel

class LootBoxCompensationTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(LootBoxCompensationTooltipModel, self).__init__(properties=properties, commands=commands)

    def getIconBefore(self):
        return self._getString(0)

    def setIconBefore(self, value):
        self._setString(0, value)

    def getIconAfter(self):
        return self._getString(1)

    def setIconAfter(self, value):
        self._setString(1, value)

    def getLabelBefore(self):
        return self._getString(2)

    def setLabelBefore(self, value):
        self._setString(2, value)

    def getLabelAfter(self):
        return self._getString(3)

    def setLabelAfter(self, value):
        self._setString(3, value)

    def getBonusName(self):
        return self._getString(4)

    def setBonusName(self, value):
        self._setString(4, value)

    def getTooltipType(self):
        return self._getString(5)

    def setTooltipType(self, value):
        self._setString(5, value)

    def getCountBefore(self):
        return self._getNumber(6)

    def setCountBefore(self, value):
        self._setNumber(6, value)

    def _initialize(self):
        super(LootBoxCompensationTooltipModel, self)._initialize()
        self._addStringProperty('iconBefore', '')
        self._addStringProperty('iconAfter', '')
        self._addStringProperty('labelBefore', '')
        self._addStringProperty('labelAfter', '')
        self._addStringProperty('bonusName', '')
        self._addStringProperty('tooltipType', 'base')
        self._addNumberProperty('countBefore', 1)
