# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/tooltips/frontline_lobby_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/tooltips/frontline_lobby_builders.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips.builders import DataBuilder, AdvancedDataBuilder, AdvancedTooltipWindowBuilder
from frontline.gui.Scaleform.daapi.view.lobby.tooltips.instruction import EpicBattleInstructionTooltipData, EpicBattleTokenInstructionContext
from frontline.gui.Scaleform.daapi.view.lobby.tooltips.recertification_tooltip import EpicBattleRecertificationFormTooltipAdvanced, EpicBattleBlanksContext, EpicBattleRecertificationFormTooltip
from frontline.gui.Scaleform.daapi.view.lobby.tooltips.epic_battle_calendar_tooltip import EpicBattleCalendarTooltip
from frontline.gui.Scaleform.daapi.view.lobby.tooltips.epic_battle_selector_tooltip import EpicBattleSelectorTooltip
from frontline.gui.Scaleform.daapi.view.lobby.tooltips.epic_battle_widget_tooltip import EpicBattleWidgetTooltip
from frontline.gui.Scaleform.daapi.view.battle.tooltips.epic_quests_tooltips import EpicBattleQuestsTooltipData, CompletedQuestsTooltipData
from frontline.gui.Scaleform.daapi.view.battle.tooltips.epic_skills import EpicSkillBaseTooltipData, EpicSkillSlotTooltip, EpicSkillSlotTooltipAdvanced, EpicSkillSlotSetupInfoTooltip
from frontline.gui.Scaleform.daapi.view.lobby.tooltips import frontline
from frontline.gui.impl.lobby.tooltips.battle_ability_alt_tooltip import BattleAbilityAltTooltipData
from frontline.gui.impl.lobby.tooltips.battle_ability_tooltip import BattleAbilityTooltipData
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.EPIC_SKILL_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, EpicSkillBaseTooltipData(contexts.QuestsBoosterContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.EPIC_SKILL_SLOT_SETUP_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, EpicSkillSlotSetupInfoTooltip(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.EPIC_QUESTS_PREVIEW, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, EpicBattleQuestsTooltipData(contexts.QuestsBoosterContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.EPIC_BATTLE_COMPLETED_QUESTS_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, CompletedQuestsTooltipData(contexts.QuestsBoosterContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.EPIC_BATTLE_SELECTOR_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, EpicBattleSelectorTooltip(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.EPIC_BATTLE_WIDGET_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, EpicBattleWidgetTooltip(contexts.ToolTipContext(None))),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.EPIC_BATTLE_RECERTIFICATION_FORM_TOOLTIP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, EpicBattleRecertificationFormTooltip(EpicBattleBlanksContext()), EpicBattleRecertificationFormTooltipAdvanced(EpicBattleBlanksContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.EPIC_BATTLE_CALENDAR_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, EpicBattleCalendarTooltip(contexts.ToolTipContext(None))),
     DataBuilder(TOOLTIPS_CONSTANTS.EPIC_BATTLE_INSTRUCTION_TOOLTIP, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, EpicBattleInstructionTooltipData(EpicBattleTokenInstructionContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.FRONTLINE_COUPON, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, frontline.FrontlinePackPreviewTooltipData(contexts.HangarContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.FRONTLINE_RANK, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, frontline.FrontlineRankTooltipData(contexts.HangarContext())),
     AdvancedTooltipWindowBuilder(TOOLTIPS_CONSTANTS.FRONTLINE_BATTLE_ABILITY, None, BattleAbilityTooltipData(contexts.ToolTipContext(None)), BattleAbilityAltTooltipData(contexts.ToolTipContext(None))),
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.EPIC_SKILL_SLOT_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, EpicSkillSlotTooltip(contexts.ToolTipContext(None)), EpicSkillSlotTooltipAdvanced(contexts.HangarCardContext())))
