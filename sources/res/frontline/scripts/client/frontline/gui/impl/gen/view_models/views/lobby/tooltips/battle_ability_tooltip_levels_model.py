# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/tooltips/battle_ability_tooltip_levels_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/tooltips/battle_ability_tooltip_levels_model.py
from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.tooltips.battle_ability_tooltip_param_model import BattleAbilityTooltipParamModel

class BattleAbilityTooltipLevelsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BattleAbilityTooltipLevelsModel, self).__init__(properties=properties, commands=commands)

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)

    def getParams(self):
        return self._getArray(1)

    def setParams(self, value):
        self._setArray(1, value)

    @staticmethod
    def getParamsType():
        return BattleAbilityTooltipParamModel

    def _initialize(self):
        super(BattleAbilityTooltipLevelsModel, self)._initialize()
        self._addNumberProperty('level', 0)
        self._addArrayProperty('params', Array())
