# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/progression_widget_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/progression_widget_tooltip.py
from __future__ import absolute_import
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController
from battle_royale.gui.impl.lobby.br_helpers.utils import setEventInfo
from battle_royale.gui.impl.gen.view_models.views.lobby.views.widget.progression_model import ProgressionModel, ProgressionStatus
from battle_royale.gui.shared.tooltips.helper import fillProgressionPointsTableModel
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IBattleRoyaleController

class ProgressionWidgetTooltipView(ViewImpl):
    __battleRoyale = dependency.descriptor(IBattleRoyaleController)
    __brProgression = dependency.descriptor(IBRProgressionOnTokensController)

    def __init__(self):
        settings = ViewSettings(R.views.battle_royale.mono.lobby.tooltips.progression_widget())
        settings.model = ProgressionModel()
        super(ProgressionWidgetTooltipView, self).__init__(settings)

    @property
    def viewModel(self):
        return super(ProgressionWidgetTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(ProgressionWidgetTooltipView, self)._onLoading(args, kwargs)
        with self.viewModel.transaction() as tx:
            if self.__brProgression.isEnabled:
                tx.setIsCompleted(self.__brProgression.isFinished)
                self.viewModel.setTimeTillEnd(self.__battleRoyale.getTimeLeftTillCycleEnd())
                fillProgressionPointsTableModel(tx.leaderBoard, self.__battleRoyale.getProgressionPointsTableData())
                status = ProgressionStatus.ACTIVE
            else:
                status = ProgressionStatus.DISABLED
            tx.setStatus(status)
            setEventInfo(tx.eventInfo)
