# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/skill/skill_extended_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/skill/skill_extended_model.py
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_model import SkillModel

class SkillExtendedModel(SkillModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(SkillExtendedModel, self).__init__(properties=properties, commands=commands)

    def getUserName(self):
        return self._getString(7)

    def setUserName(self, value):
        self._setString(7, value)

    def getDescription(self):
        return self._getString(8)

    def setDescription(self, value):
        self._setString(8, value)

    def _initialize(self):
        super(SkillExtendedModel, self)._initialize()
        self._addStringProperty('userName', '')
        self._addStringProperty('description', '')
