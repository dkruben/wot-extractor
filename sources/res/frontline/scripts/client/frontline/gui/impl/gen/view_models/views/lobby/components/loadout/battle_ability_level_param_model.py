# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/components/loadout/battle_ability_level_param_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/components/loadout/battle_ability_level_param_model.py
from frameworks.wulf import ViewModel

class BattleAbilityLevelParamModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(BattleAbilityLevelParamModel, self).__init__(properties=properties, commands=commands)

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)

    def getValueTemplate(self):
        return self._getString(1)

    def setValueTemplate(self, value):
        self._setString(1, value)

    def getValue(self):
        return self._getString(2)

    def setValue(self, value):
        self._setString(2, value)

    def getName(self):
        return self._getString(3)

    def setName(self, value):
        self._setString(3, value)

    def getSign(self):
        return self._getString(4)

    def setSign(self, value):
        self._setString(4, value)

    def _initialize(self):
        super(BattleAbilityLevelParamModel, self)._initialize()
        self._addStringProperty('id', '')
        self._addStringProperty('valueTemplate', '')
        self._addStringProperty('value', '')
        self._addStringProperty('name', '')
        self._addStringProperty('sign', '')
