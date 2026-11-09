# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/personal_case/tankman_skill_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/personal_case/tankman_skill_model.py
from enum import Enum
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_extended_model import SkillExtendedModel

class AnimationType(Enum):
    NONE = 'none'
    UNLOCKED = 'unlocked'
    SELECTED = 'selected'


class TankmanSkillModel(SkillExtendedModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(TankmanSkillModel, self).__init__(properties=properties, commands=commands)

    def getIsDisabled(self):
        return self._getBool(9)

    def setIsDisabled(self, value):
        self._setBool(9, value)

    def getIsLocked(self):
        return self._getBool(10)

    def setIsLocked(self, value):
        self._setBool(10, value)

    def getAnimationType(self):
        return AnimationType(self._getString(11))

    def setAnimationType(self, value):
        self._setString(11, value.value)

    def _initialize(self):
        super(TankmanSkillModel, self)._initialize()
        self._addBoolProperty('isDisabled', False)
        self._addBoolProperty('isLocked', False)
        self._addStringProperty('animationType', AnimationType.NONE.value)
