# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/progress_counter/state_machine/states.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/pve_base/progress_counter/state_machine/states.py
from __future__ import absolute_import
from frameworks_common.state_machine import StateFlags
from gui.Scaleform.daapi.view.battle.pve_base.base.state_machine.states import BaseState
from pve_battle_hud import ProgressCounterState

class InitialState(BaseState):
    __slots__ = ()

    def __init__(self):
        super(InitialState, self).__init__(stateID=ProgressCounterState.INITIAL, flags=StateFlags.INITIAL)


class BaseProgressCounterState(BaseState):

    def _showProgress(self, isAnimated):
        serverSettings, clientSettings = self.getSettings()
        icon = clientSettings.icon
        title = clientSettings.getHeader(serverSettings.params)
        self._view.as_setDataS(icon, title, isAnimated=isAnimated)

    def _updateView(self):
        self._showProgress(isAnimated=True)


class AppearanceState(BaseProgressCounterState):
    __slots__ = ()

    def __init__(self):
        super(AppearanceState, self).__init__(stateID=ProgressCounterState.APPEARANCE, flags=StateFlags.UNDEFINED)

    def _showView(self):
        self._showProgress(isAnimated=True)


class RegularState(BaseProgressCounterState):
    __slots__ = ()

    def __init__(self):
        super(RegularState, self).__init__(stateID=ProgressCounterState.REGULAR, flags=StateFlags.UNDEFINED)

    def _showView(self):
        self._showProgress(isAnimated=False)


class HiddenState(BaseState):
    __slots__ = ()

    def __init__(self):
        super(HiddenState, self).__init__(stateID=ProgressCounterState.HIDDEN, flags=StateFlags.FINAL)

    def _showView(self):
        self._view.as_setDataS('', '', isAnimated=True)
