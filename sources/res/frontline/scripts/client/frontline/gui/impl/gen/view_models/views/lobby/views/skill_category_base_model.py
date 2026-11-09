# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/skill_category_base_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/skill_category_base_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.skill_base_model import SkillBaseModel

class SkillCategoryType(Enum):
    FIRESUPPORT = 'firesupport'
    RECONNAISSANCE = 'reconnaissance'
    TACTICS = 'tactics'


class SkillCategoryBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SkillCategoryBaseModel, self).__init__(properties=properties, commands=commands)

    def getType(self):
        return SkillCategoryType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)

    def getSkills(self):
        return self._getArray(1)

    def setSkills(self, value):
        self._setArray(1, value)

    @staticmethod
    def getSkillsType():
        return SkillBaseModel

    def _initialize(self):
        super(SkillCategoryBaseModel, self)._initialize()
        self._addStringProperty('type')
        self._addArrayProperty('skills', Array())
