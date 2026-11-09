# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/tankman_tooltip_modifier_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/tankman_tooltip_modifier_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class TankmanTooltipModifierModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TankmanTooltipModifierModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getReal(0)

    def setValue(self, value):
        self._setReal(0, value)

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)

    def getTitle(self):
        return self._getString(2)

    def setTitle(self, value):
        self._setString(2, value)

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(TankmanTooltipModifierModel, self)._initialize()
        self._addRealProperty('value', 0.0)
        self._addResourceProperty('icon', R.invalid())
        self._addStringProperty('title', '')
        self._addStringProperty('description', '')
