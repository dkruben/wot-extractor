# wot-extractor: codigo DESCOMPILADO de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/fort_rush_progression_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fort_rush/scripts/client/fort_rush/gui/impl/lobby/fort_rush_progression_view.py
from __future__ import absolute_import
from fort_rush.gui.impl.lobby.presenters.fort_rush_progression_presenter import FortRushProgressionPresenter
from fort_rush.gui.sounds.sound_constants import FORT_RUSH_PROGRESSION_SOUND_SPACE
from frameworks.wulf import ViewFlags, ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from fort_rush.gui.impl.gen.view_models.views.progression.progression_view_model import ProgressionViewModel

class FortRushProgressionView(ViewImpl):
    _COMMON_SOUND_SPACE = FORT_RUSH_PROGRESSION_SOUND_SPACE

    def __init__(self, layoutId):
        viewModel = ProgressionViewModel()
        settings = ViewSettings(layoutId, flags=ViewFlags.LOBBY_TOP_SUB_VIEW, model=viewModel)
        super(FortRushProgressionView, self).__init__(settings)
        self.__presenter = FortRushProgressionPresenter(viewModel, self)

    @property
    def viewModel(self):
        return super(FortRushProgressionView, self).getViewModel()

    def createToolTip(self, event):
        if event.contentID != R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            return super(FortRushProgressionView, self).createToolTip(event)
        else:
            self.__presenter.createToolTip(event)
            return

    def createToolTipContent(self, event, contentID):
        content = self.__presenter.createToolTipContent(event, contentID)
        if content is not None:
            return content
        else:
            return super(FortRushProgressionView, self).createToolTipContent(event, contentID)

    def _onLoaded(self, *args, **kwargs):
        super(FortRushProgressionView, self)._onLoaded(*args, **kwargs)
        self.__presenter.saveSeenProgress()

    def _onLoading(self, *args, **kwargs):
        super(FortRushProgressionView, self)._onLoading(*args, **kwargs)
        self.__presenter.initialize()
        self.__presenter.packModel()

    def _finalize(self):
        self.__presenter.finalize()
        super(FortRushProgressionView, self)._finalize()
