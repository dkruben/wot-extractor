# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/progress_counter/progress_counter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/pve_base/progress_counter/progress_counter.py
from __future__ import absolute_import
import BattleReplay
from gui.Scaleform.daapi.view.battle.pve_base.base.pve_hud_widget import SingleItemPveHudWidget
from gui.Scaleform.daapi.view.battle.pve_base.progress_counter.settings_model import ProgressCounterServerModel
from gui.Scaleform.daapi.view.battle.pve_base.progress_counter.state_machine.machine import ProgressCounterStateMachine
from gui.Scaleform.daapi.view.meta.PveProgressCounterMeta import PveProgressCounterMeta
from pve_battle_hud import WidgetType, ProgressCounterState

class PveProgressCounter(SingleItemPveHudWidget, PveProgressCounterMeta):

    def __init__(self):
        super(PveProgressCounter, self).__init__(widgetType=WidgetType.PROGRESS_COUNTER, stateMachineClass=ProgressCounterStateMachine, serverSettingsModel=ProgressCounterServerModel)

    def _getStateToRestore(self, serverSettings):
        serverState = serverSettings.state
        if serverState == ProgressCounterState.HIDDEN:
            return None
        else:
            if serverState in [ProgressCounterState.APPEARANCE, ProgressCounterState.REGULAR]:
                return ProgressCounterState.REGULAR
            return serverState

    def _onPrebattlePeriod(self):
        if BattleReplay.isPlaying():
            self.as_setDataS('', '', False)
