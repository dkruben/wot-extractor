# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/skill_select_item_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_compare/skill_select_item_model.py
from enum import Enum
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_simple_model import SkillSimpleModel

class SkillState(Enum):
    DEFAULT = 'default'
    SELECTED = 'selected'
    DISABLED = 'disabled'


class SkillType(Enum):
    MAJOR = 'major'
    COMMON = 'common'
    BONUS = 'bonus'


class SkillSelectItemModel(SkillSimpleModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SkillSelectItemModel, self).__init__(properties=properties, commands=commands)

    def getState(self):
        return SkillState(self._getString(4))

    def setState(self, value):
        self._setString(4, value.value)

    def _initialize(self):
        super(SkillSelectItemModel, self)._initialize()
        self._addStringProperty('state')
