# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/tooltip/post_progression_level_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/tooltip/post_progression_level_tooltip_view_model.py
from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel

class ModificationType(Enum):
    NONE = 'none'
    PAIRMODIFICATION = 'pairModification'
    FEATURE = 'feature'


class PostProgressionLevelTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(PostProgressionLevelTooltipViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def modifier(self):
        return self._getViewModel(0)

    @staticmethod
    def getModifierType():
        return BonusesModel

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)

    def getType(self):
        return ModificationType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)

    def getNameRes(self):
        return self._getResource(3)

    def setNameRes(self, value):
        self._setResource(3, value)

    def getIsUnlocked(self):
        return self._getBool(4)

    def setIsUnlocked(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(PostProgressionLevelTooltipViewModel, self)._initialize()
        self._addViewModelProperty('modifier', BonusesModel())
        self._addNumberProperty('level', 0)
        self._addStringProperty('type')
        self._addResourceProperty('nameRes', R.invalid())
        self._addBoolProperty('isUnlocked', False)
