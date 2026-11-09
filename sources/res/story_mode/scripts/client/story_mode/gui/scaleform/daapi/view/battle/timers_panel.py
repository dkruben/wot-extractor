# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/timers_panel.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/timers_panel.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.timers_panel import TimersPanel
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_COLORS import BATTLE_NOTIFICATIONS_TIMER_COLORS
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_LINKAGES import BATTLE_NOTIFICATIONS_TIMER_LINKAGES
from gui.Scaleform.genConsts.BATTLE_NOTIFICATIONS_TIMER_TYPES import BATTLE_NOTIFICATIONS_TIMER_TYPES
from gui.impl import backport
from gui.impl.gen import R
_OVERTURNED_LINKAGE = 'StoryModeDestroyTimerUI'
_OVERTURNED_ICON = 'StoryModeOverturnIconUI'
_OVERTURNED_ICON_OFFSET = -20

class StoryModelTimersPanel(TimersPanel):

    def _generateMainTimersData(self):
        return [
         self._getNotificationTimerData(BATTLE_NOTIFICATIONS_TIMER_TYPES.DROWN, BATTLE_NOTIFICATIONS_TIMER_LINKAGES.DROWN_ICON, BATTLE_NOTIFICATIONS_TIMER_LINKAGES.DESTROY_TIMER_UI),
         self._getNotificationTimerData(BATTLE_NOTIFICATIONS_TIMER_TYPES.OVERTURNED, _OVERTURNED_ICON, _OVERTURNED_LINKAGE, BATTLE_NOTIFICATIONS_TIMER_COLORS.GREEN, text=backport.text(R.strings.sm_battle.timersPanel.overturned()), iconOffsetY=_OVERTURNED_ICON_OFFSET)]
