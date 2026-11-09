# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/tooltips/level_reserves_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/tooltips/level_reserves_tooltip_model.py
from frameworks.wulf import Array, ViewModel

class LevelReservesTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LevelReservesTooltipModel, self).__init__(properties=properties, commands=commands)

    def getLevels(self):
        return self._getArray(0)

    def setLevels(self, value):
        self._setArray(0, value)

    @staticmethod
    def getLevelsType():
        return unicode

    def getHasOptionalReserves(self):
        return self._getBool(1)

    def setHasOptionalReserves(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(LevelReservesTooltipModel, self)._initialize()
        self._addArrayProperty('levels', Array())
        self._addBoolProperty('hasOptionalReserves', False)
