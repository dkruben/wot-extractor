# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/daily_section/presenters/base_missions_block_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/daily_section/presenters/base_missions_block_presenter.py
from __future__ import absolute_import
import typing
from gui.impl.lobby.user_missions.hangar_widget.utils import DailyMissionItemPacker
from gui.impl.lobby.user_missions.hub.tabs.basic.daily_section.presenters.base_block_presenter import BaseBlockPresenter
from gui.impl.pub.view_impl import TViewModel
from gui.shared.missions.packers.bonus import getDailyMissionsBonusPacker
from gui.shared.missions.packers.events import packQuestBonusModelAndTooltipData
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.common.mission_base_model import MissionBaseModel
    from gui.server_events.event_items import Quest

class BaseMissionsBlockPresenter(BaseBlockPresenter[TViewModel]):

    def __init__(self, model):
        super(BaseMissionsBlockPresenter, self).__init__(model=model)

    def _onLeaveTab(self):
        with self.getViewModel().transaction() as tx:
            self._disableCompletedQuestAnimation(tx)

    def _fillMissionModel(self, mm, quest):
        dailyPacker = DailyMissionItemPacker()
        isCompleted = dailyPacker.packMissionItem(mm, quest)
        questID = quest.getID()
        mm.setId(questID)
        self._tooltipData[questID] = {}
        packQuestBonusModelAndTooltipData(getDailyMissionsBonusPacker(), mm.getBonuses(), quest, tooltipData=self._tooltipData[questID])
        self._rewardsGetterByQuestID[questID] = mm.getBonuses
        return isCompleted

    def _disableCompletedQuestAnimation(self, vm):
        missionsList = vm.getMissionsList()
        for m in missionsList:
            m.setAnimateCompletion(False)
            m.setEarned(0)

        missionsList.invalidate()
