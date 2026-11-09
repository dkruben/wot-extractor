# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_progression_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_progression_tooltip_view.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunProgressionWatcher, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_progression_tooltip_view_model import FunRandomProgressionTooltipViewModel
from fun_random.gui.impl.lobby.common.fun_view_helpers import packProgressionActiveStage, packProgressionState, packInfiniteProgressionState, packInfiniteProgressionStage, packInfiniteProgressionConditions, packProgressionConditions
from gui.impl.gen import R
from gui.impl.pub import ViewImpl

class FunRandomProgressionTooltipView(ViewImpl, FunAssetPacksMixin, FunProgressionWatcher, FunSubModesWatcher):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(layoutID=R.views.fun_random.mono.lobby.tooltips.progression_tooltip(), model=FunRandomProgressionTooltipViewModel())
        super(FunRandomProgressionTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(FunRandomProgressionTooltipView, self).getViewModel()

    def _finalize(self):
        self.stopProgressionListening(self.__invalidateAll, tickMethod=self.__invalidateTimer)

    def _onLoading(self, *args, **kwargs):
        super(FunRandomProgressionTooltipView, self)._onLoading(*args, **kwargs)
        self.startProgressionListening(self.__invalidateAll, tickMethod=self.__invalidateTimer)
        self.__invalidateAll()

    @hasActiveProgression()
    def __invalidateAll(self, *_):
        progression = self.getActiveProgression()
        with self.viewModel.transaction() as model:
            model.setAssetsPointer(self.getModeAssetsPointer())
            model.setIsMultipleSubModes(len(self.getSubModes()) > 1)
            if progression.isInUnlimitedProgression:
                packInfiniteProgressionState(progression, model.state)
                packInfiniteProgressionStage(progression, model.currentStage, isSpecial=True)
                packInfiniteProgressionConditions(progression, model.condition)
            else:
                packProgressionState(progression, model.state)
                packProgressionActiveStage(progression, model.currentStage, isSpecial=True)
                packProgressionConditions(progression, model.condition)

    @hasActiveProgression()
    def __invalidateTimer(self, *_):
        self.viewModel.state.setStatusTimer(self.getActiveProgression().statusTimer)
