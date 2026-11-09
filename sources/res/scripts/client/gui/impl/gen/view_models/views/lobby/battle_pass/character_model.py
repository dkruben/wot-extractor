# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/character_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/character_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.skill_model import SkillModel

class CharacterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(CharacterModel, self).__init__(properties=properties, commands=commands)

    def getTankman(self):
        return self._getString(0)

    def setTankman(self, value):
        self._setString(0, value)

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)

    def getSkills(self):
        return self._getArray(2)

    def setSkills(self, value):
        self._setArray(2, value)

    @staticmethod
    def getSkillsType():
        return SkillModel

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)

    def getGroupName(self):
        return self._getString(4)

    def setGroupName(self, value):
        self._setString(4, value)

    def getHasVoice(self):
        return self._getBool(5)

    def setHasVoice(self, value):
        self._setBool(5, value)

    def _initialize(self):
        super(CharacterModel, self)._initialize()
        self._addStringProperty('tankman', '')
        self._addStringProperty('icon', '')
        self._addArrayProperty('skills', Array())
        self._addStringProperty('tooltipId', '')
        self._addStringProperty('groupName', '')
        self._addBoolProperty('hasVoice', False)
