# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/state_machine/states/idle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/state_machine/states/idle.py
from frameworks_common.state_machine import StateFlags
import game_loading_bindings
from gui.game_loading import loggers
from gui.game_loading.state_machine.states.base import BaseState
from gui.game_loading.state_machine.const import GameLoadingStates, LOADING_VIEW_FADE_OUT_DURATION
_logger = loggers.getStatesLogger()

class IdleState(BaseState):
    __slots__ = ()

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(IdleState, self).__init__(stateID=GameLoadingStates.IDLE.value, flags=flags)

    def _onEntered(self, event):
        super(IdleState, self)._onEntered(event)
        if game_loading_bindings.isViewOpened():
            _logger.debug('[%s] closing GF view.', self)
            game_loading_bindings.destroyLoadingView(LOADING_VIEW_FADE_OUT_DURATION)
        _logger.debug('[%s] entered.', self)
