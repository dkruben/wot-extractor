# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/tooltips/fun_random_progression_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/tooltips/fun_random_progression_tooltip_view_model.py
from frameworks.wulf import ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_stage import FunRandomProgressionStage
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState

class FunRandomProgressionTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(FunRandomProgressionTooltipViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def state(self):
        return self._getViewModel(0)

    @staticmethod
    def getStateType():
        return FunRandomProgressionState

    @property
    def condition(self):
        return self._getViewModel(1)

    @staticmethod
    def getConditionType():
        return FunRandomProgressionCondition

    @property
    def currentStage(self):
        return self._getViewModel(2)

    @staticmethod
    def getCurrentStageType():
        return FunRandomProgressionStage

    def getAssetsPointer(self):
        return self._getString(3)

    def setAssetsPointer(self, value):
        self._setString(3, value)

    def getIsMultipleSubModes(self):
        return self._getBool(4)

    def setIsMultipleSubModes(self, value):
        self._setBool(4, value)

    def _initialize(self):
        super(FunRandomProgressionTooltipViewModel, self)._initialize()
        self._addViewModelProperty('state', FunRandomProgressionState())
        self._addViewModelProperty('condition', FunRandomProgressionCondition())
        self._addViewModelProperty('currentStage', FunRandomProgressionStage())
        self._addStringProperty('assetsPointer', 'undefined')
        self._addBoolProperty('isMultipleSubModes', True)
