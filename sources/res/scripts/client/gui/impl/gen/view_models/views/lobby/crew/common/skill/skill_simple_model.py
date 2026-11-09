# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/skill/skill_simple_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/skill/skill_simple_model.py
from frameworks.wulf import ViewModel

class SkillSimpleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SkillSimpleModel, self).__init__(properties=properties, commands=commands)

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)

    def getIconName(self):
        return self._getString(1)

    def setIconName(self, value):
        self._setString(1, value)

    def getRoleName(self):
        return self._getString(2)

    def setRoleName(self, value):
        self._setString(2, value)

    def getLevel(self):
        return self._getReal(3)

    def setLevel(self, value):
        self._setReal(3, value)

    def _initialize(self):
        super(SkillSimpleModel, self)._initialize()
        self._addStringProperty('name', '')
        self._addStringProperty('iconName', '')
        self._addStringProperty('roleName', '')
        self._addRealProperty('level', 0.0)
