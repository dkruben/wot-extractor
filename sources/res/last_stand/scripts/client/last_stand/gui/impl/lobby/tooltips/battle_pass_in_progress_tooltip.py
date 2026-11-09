# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/battle_pass_in_progress_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/battle_pass_in_progress_tooltip.py
from __future__ import absolute_import
from gui.impl.gen import R
from gui.impl.lobby.battle_pass.tooltips.battle_pass_in_progress_tooltip_view import BattlePassInProgressTooltipView

class LSBattlePassInProgressTooltipView(BattlePassInProgressTooltipView):
    LAYOUT_ID = R.views.last_stand.mono.lobby.tooltips.battle_pass_tooltip()

    def _hasRewardPoints(self):
        return False
