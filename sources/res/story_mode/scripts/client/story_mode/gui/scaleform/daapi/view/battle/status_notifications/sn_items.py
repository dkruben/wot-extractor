# wot-extractor: codigo DESCOMPILADO de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/status_notifications/sn_items.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/status_notifications/sn_items.py
from __future__ import absolute_import
import typing, BigWorld
from gui.Scaleform.daapi.view.battle.shared.status_notifications.sn_items import TimerSN
from gui.impl import backport
from story_mode.gui.battle_control.battle_constant import VEHICLE_VIEW_STATE
from story_mode.gui.scaleform.genConsts.STORY_MODE_NOTIFICATIONS_TIMER_TYPES import STORY_MODE_NOTIFICATIONS_TIMER_TYPES
from story_mode_common.story_mode_constants import RECON_ABILITY

class ReconAbilitySN(TimerSN):

    def _getEquipmentName(self):
        return RECON_ABILITY

    def getItemID(self):
        return ''

    def getViewTypeID(self):
        return STORY_MODE_NOTIFICATIONS_TIMER_TYPES.RECON_ABILITY

    def _getDescription(self, value):
        return backport.text(value)

    def _update(self, value):
        if not value:
            self._setVisible(False)
            return
        self._setVisible(True)
        self._updateText(value['text'])
        self._updateTimeParams(value['totalTime'], value['finishTime'])
        self._sendUpdate()


class DisableShotSN(TimerSN):

    def start(self):
        super(DisableShotSN, self).start()
        self._subscribeOnVehControlling()

    def getItemID(self):
        return VEHICLE_VIEW_STATE.SCC_DISABLE_SHOT

    def getViewTypeID(self):
        return STORY_MODE_NOTIFICATIONS_TIMER_TYPES.SCC_DISABLE_SHOT

    def _update(self, value):
        if value > 0.0:
            endTime = BigWorld.serverTime() + value
            self._updateTimeParams(value, endTime)
            self._setVisible(True)
        else:
            self._setVisible(False)
