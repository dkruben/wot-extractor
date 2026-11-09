# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/prestige/prestige_emblem_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/prestige/prestige_emblem_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class PrestigeLevelGrade(Enum):
    IRON = 'iron'
    BRONZE = 'bronze'
    SILVER = 'silver'
    GOLD = 'gold'
    ENAMEL = 'enamel'
    MAXIMUM = 'prestige'
    UNDEFINED = 'undefined'


class PrestigeEmblemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PrestigeEmblemModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return PrestigeLevelGrade(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)

    def getGrade(self):
        return self._getNumber(2)

    def setGrade(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(PrestigeEmblemModel, self)._initialize()
        self._addStringProperty('type')
        self._addNumberProperty('level', 0)
        self._addNumberProperty('grade', -1)
