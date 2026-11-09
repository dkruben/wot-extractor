# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_pass/battle_pass_decorators.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_pass/battle_pass_decorators.py
from __future__ import absolute_import
import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.battle_pass.tooltips.battle_pass_coin_tooltip_view import BattlePassCoinTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_gold_mission_tooltip_view import BattlePassGoldMissionTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_lock_icon_tooltip_view import BattlePassLockIconTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_points_view import BattlePassPointsTooltip
from gui.impl.lobby.battle_pass.tooltips.battle_pass_quests_chain_tooltip_view import BattlePassQuestsChainTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_taler_tooltip import BattlePassTalerTooltip
from gui.impl.lobby.battle_pass.tooltips.battle_pass_upgrade_style_tooltip_view import BattlePassUpgradeStyleTooltipView
from gui.impl.lobby.battle_pass.tooltips.crew_member_skill_tooltip import CrewMemberSkillTooltip
from gui.impl.lobby.battle_pass.tooltips.random_quest_tooltip import RandomQuestTooltip
from gui.impl.lobby.battle_pass.tooltips.reward_compensation_tooltip import RewardCompensationTooltip
from gui.impl.lobby.lootbox_system.base.tooltips.box_tooltip import BoxTooltip
if typing.TYPE_CHECKING:
    from gui.impl.backport import TooltipData

def createBackportTooltipDecorator():

    def decorator(func):

        def wrapper(self, event):
            if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
                tooltipData = self.getTooltipData(event)
                if tooltipData is None:
                    return
                window = backport.BackportTooltipWindow(tooltipData, self.getParentWindow(), event)
                if window is None:
                    return
                window.load()
                return window
            else:
                return func(self, event)

        return wrapper

    return decorator


def createTooltipContentDecorator():

    def decorator(func):

        def wrapper(self, event, contentID):
            tooltipData = self.getTooltipData(event)
            if contentID == R.views.mono.battle_pass.tooltips.gold_mission():
                if tooltipData is None:
                    return
                return BattlePassGoldMissionTooltipView(*tooltipData.specialArgs)
            else:
                if contentID == R.views.mono.battle_pass.tooltips.upgrade_style():
                    if tooltipData is None:
                        return
                    return BattlePassUpgradeStyleTooltipView(*tooltipData.specialArgs)
                if contentID == R.views.mono.battle_pass.tooltips.quest_chain():
                    if tooltipData is None:
                        return
                    return BattlePassQuestsChainTooltipView(*tooltipData.specialArgs)
                if contentID == R.views.mono.battle_pass.tooltips.random_quest():
                    if event.hasArgument('tokenID'):
                        return RandomQuestTooltip(event.getArgument('tokenID'))
                    if tooltipData is None:
                        return
                    return RandomQuestTooltip(*tooltipData.specialArgs)
                if contentID == R.views.mono.battle_pass.tooltips.bpcoin():
                    return BattlePassCoinTooltipView()
                if contentID == R.views.mono.battle_pass.tooltips.bp_points():
                    return BattlePassPointsTooltip()
                if contentID == R.views.mono.battle_pass.tooltips.lock_icon():
                    return BattlePassLockIconTooltipView()
                if contentID == R.views.mono.lootbox.tooltips.box_tooltip():
                    if tooltipData is None:
                        return
                    return BoxTooltip(*tooltipData.specialArgs)
                if contentID == R.views.mono.battle_pass.tooltips.bptaler():
                    return BattlePassTalerTooltip()
                if contentID == R.views.mono.battle_pass.tooltips.reward_compensation():
                    return RewardCompensationTooltip(*tooltipData.specialArgs)
                if contentID == R.views.mono.battle_pass.tooltips.crew_member_skill():
                    return CrewMemberSkillTooltip(event.getArgument('name'), event.getArgument('isZero'), event.getArgument('hasZeroPerk'))
                return func(self, event, contentID)

        return wrapper

    return decorator
