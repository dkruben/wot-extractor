# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/difficulty_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/lobby/tooltips/difficulty_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from halloween.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel

class DifficultyTooltipView(ViewImpl):
    __slots__ = ('__level', '__state', '__isLocked')

    def __init__(self, level, state, isLocked, layoutID=R.views.halloween.mono.lobby.tooltips.difficulty_tooltip()):
        settings = ViewSettings(layoutID)
        settings.model = DifficultyItemModel()
        super(DifficultyTooltipView, self).__init__(settings)
        self.__level = level
        self.__state = state
        self.__isLocked = isLocked

    @property
    def viewModel(self):
        return super(DifficultyTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(DifficultyTooltipView, self)._onLoading()
        with self.viewModel.transaction() as model:
            model.setLevel(self.__level)
            model.setState(self.__state)
            model.setIsLocked(self.__isLocked)
