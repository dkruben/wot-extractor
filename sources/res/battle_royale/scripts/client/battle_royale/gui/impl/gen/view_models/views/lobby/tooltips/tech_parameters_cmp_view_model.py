# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/tech_parameters_cmp_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/tooltips/tech_parameters_cmp_view_model.py
from frameworks.wulf import ViewModel

class TechParametersCmpViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(TechParametersCmpViewModel, self).__init__(properties=properties, commands=commands)

    def getDifficulty(self):
        return self._getNumber(0)

    def setDifficulty(self, value):
        self._setNumber(0, value)

    def getSpotting(self):
        return self._getNumber(1)

    def setSpotting(self, value):
        self._setNumber(1, value)

    def getMobility(self):
        return self._getNumber(2)

    def setMobility(self, value):
        self._setNumber(2, value)

    def getSurvivability(self):
        return self._getNumber(3)

    def setSurvivability(self, value):
        self._setNumber(3, value)

    def getDamage(self):
        return self._getNumber(4)

    def setDamage(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(TechParametersCmpViewModel, self)._initialize()
        self._addNumberProperty('difficulty', 0)
        self._addNumberProperty('spotting', 0)
        self._addNumberProperty('mobility', 0)
        self._addNumberProperty('survivability', 0)
        self._addNumberProperty('damage', 0)
