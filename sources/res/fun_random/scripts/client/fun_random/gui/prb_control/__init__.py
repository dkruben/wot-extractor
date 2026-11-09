# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/__init__.py
from __future__ import absolute_import
from constants import PREBATTLE_TYPE, QUEUE_TYPE
from fun_random_common.fun_constants import ARENA_BONUS_TYPE
from fun_random.gui.battle_results.fun_stats_controller import FunBattleResultStatsCtrl
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin
from fun_random.gui.impl.lobby.tooltips.fun_random_progression_tooltip_view import FunRandomProgressionTooltipView
from fun_random.gui.prb_control.formatters.invites import FunPrbInviteHtmlTextFormatter
from fun_random.gui.prb_control.storages.fun_random_storage import FunRandomStorage
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.mode_selector.tooltips.mode_selector_tooltips_constants import ModeSelectorTooltipsConstants
from gui.prb_control.storages import makeQueueName
from gui.shared.system_factory import registerPrbInviteHtmlFormatter, registerPrbStorage, registerModeSelectorTooltips, registerModeNameKwargsGetterByPrb, registerModeNameKwargsGetterByQueue, registerModeNameKwargsGetterByBonusType, registerPrebattleConditionIconGetter, registerBattleResultStatsCtrl

def registerFunRandomOthersPrbParams():
    registerModeSelectorTooltips([
     ModeSelectorTooltipsConstants.FUN_RANDOM_CALENDAR_TOOLTIP,
     ModeSelectorTooltipsConstants.FUN_RANDOM_REWARDS], {(R.views.fun_random.mono.lobby.tooltips.progression_tooltip()): FunRandomProgressionTooltipView})
    registerPrbStorage(makeQueueName(QUEUE_TYPE.FUN_RANDOM), FunRandomStorage())
    registerPrbInviteHtmlFormatter(PREBATTLE_TYPE.FUN_RANDOM, FunPrbInviteHtmlTextFormatter)
    registerModeNameKwargsGetterByQueue(QUEUE_TYPE.FUN_RANDOM, FunAssetPacksMixin.getModeNameKwargs)
    registerModeNameKwargsGetterByPrb(PREBATTLE_TYPE.FUN_RANDOM, FunAssetPacksMixin.getModeNameKwargs)
    registerModeNameKwargsGetterByBonusType(ARENA_BONUS_TYPE.FUN_RANDOM, FunAssetPacksMixin.getModeNameKwargs)
    registerPrebattleConditionIconGetter(ARENA_BONUS_TYPE.FUN_RANDOM, FunAssetPacksMixin.getPrebattleConditionIcon)
    registerBattleResultStatsCtrl(ARENA_BONUS_TYPE.FUN_RANDOM, FunBattleResultStatsCtrl)
