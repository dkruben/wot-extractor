# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/battle_quest_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/battle_quest_tooltip.py
from __future__ import absolute_import
from comp7.gui.impl.lobby.comp7_helpers.comp7_bonus_packer import packQuestBonuses
from comp7_light.gui.impl.lobby.comp7_light_helpers.comp7_light_mission_packer import packMissionItem
from comp7_light.gui.impl.lobby.comp7_light_helpers.comp7_light_packers import getComp7LightBonusPacker
from frameworks.wulf import ViewSettings
from frameworks.wulf.view.array import fillViewModelsArray
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel
from gui.impl.lobby.user_missions.tooltips.quest_tooltip import BaseQuestTooltip
from gui.server_events.events_helpers import EventInfoModel
from gui.shared.missions.packers.events import DailyQuestUIDataPacker

class BattleQuestTooltip(BaseQuestTooltip):

    def _getSettings(self):
        settings = ViewSettings(R.views.comp7_light.mono.lobby.tooltips.battle_quest_tooltip())
        settings.model = WidgetQuestModel()
        return settings

    def _fillViewModel(self):
        bonusPacker = getComp7LightBonusPacker()
        packedBonuses, _ = packQuestBonuses(self._quest.getBonuses(), bonusPacker)
        with self.viewModel.transaction() as tx:
            packMissionItem(tx, self._quest, DailyQuestUIDataPacker)
            fillViewModelsArray(packedBonuses, tx.getBonuses())
            tx.setCountdown(EventInfoModel.getDailyProgressResetTimeDelta())

    def _getRewardsSortKey(self):
        return
