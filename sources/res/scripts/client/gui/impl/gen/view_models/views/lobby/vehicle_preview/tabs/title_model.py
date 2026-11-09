# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_preview/tabs/title_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_preview/tabs/title_model.py
from frameworks.wulf import ViewModel

class TitleModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(TitleModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)

    def getSkillName(self):
        return self._getString(1)

    def setSkillName(self, value):
        self._setString(1, value)

    def getRoleName(self):
        return self._getString(2)

    def setRoleName(self, value):
        self._setString(2, value)

    def getSkillCustomName(self):
        return self._getString(3)

    def setSkillCustomName(self, value):
        self._setString(3, value)

    def getIconName(self):
        return self._getString(4)

    def setIconName(self, value):
        self._setString(4, value)

    def _initialize(self):
        super(TitleModel, self)._initialize()
        self._addStringProperty('title', '')
        self._addStringProperty('skillName', '')
        self._addStringProperty('roleName', '')
        self._addStringProperty('skillCustomName', '')
        self._addStringProperty('iconName', '')
