# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/difficulty_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/impl/lobby/difficulty_tooltip.py
from __future__ import absolute_import
from frameworks.wulf.view.view import ViewSettings
from gui.impl.gen import R
from story_mode.gui.impl.gen.view_models.views.lobby.mission_difficulty_tooltip_model import MissionDifficultyTooltipModel
from gui.impl.pub import ViewImpl

class DifficultyTooltip(ViewImpl):

    def __init__(self, difficulty, isSelected, isLocked=False, isAutoCompleteCondition=False):
        settings = ViewSettings(R.views.story_mode.mono.lobby.tooltips.difficulty_tooltip(), model=MissionDifficultyTooltipModel())
        super(DifficultyTooltip, self).__init__(settings)
        self._difficulty = difficulty
        self._isAutoCompleteCondition = isAutoCompleteCondition
        self._isSelected = isSelected
        self._isLocked = isLocked

    @property
    def viewModel(self):
        return super(DifficultyTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(DifficultyTooltip, self)._onLoading(*args, **kwargs)
        self.viewModel.setDifficulty(self._difficulty)
        self.viewModel.setIsAutoCompleteCondition(self._isAutoCompleteCondition)
        self.viewModel.setIsSelected(self._isSelected)
        self.viewModel.setIsLocked(self._isLocked)
