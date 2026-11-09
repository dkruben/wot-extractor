# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/tooltips/fun_random_progression_quest_tooltip_view_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/tooltips/fun_random_progression_quest_tooltip_view_model.py
from frameworks.wulf import ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_quest_card_model import FunRandomQuestCardModel
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_base_quest_tooltip_view_model import FunRandomBaseQuestTooltipViewModel

class FunRandomProgressionQuestTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FunRandomProgressionQuestTooltipViewModel, self).__init__(properties=properties, commands=commands)

    @property
    def quest(self):
        return self._getViewModel(0)

    @staticmethod
    def getQuestType():
        return FunRandomQuestCardModel

    @property
    def tooltip(self):
        return self._getViewModel(1)

    @staticmethod
    def getTooltipType():
        return FunRandomBaseQuestTooltipViewModel

    def _initialize(self):
        super(FunRandomProgressionQuestTooltipViewModel, self)._initialize()
        self._addViewModelProperty('quest', FunRandomQuestCardModel())
        self._addViewModelProperty('tooltip', FunRandomBaseQuestTooltipViewModel())
