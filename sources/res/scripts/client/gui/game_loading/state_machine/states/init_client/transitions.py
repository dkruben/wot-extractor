# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/game_loading/state_machine/states/init_client/transitions.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/game_loading/state_machine/states/init_client/transitions.py
import typing
from frameworks_common.state_machine.transitions import StringEventTransition
from gui.game_loading.state_machine.const import GameLoadingStatesEvents
from gui.game_loading.state_machine.states.transitions import SourceToSingleTargetTransition
if typing.TYPE_CHECKING:
    from frameworks_common.state_machine.events import StringEvent
    from gui.game_loading.state_machine.machine import GameLoadingStateMachine
    from gui.game_loading.state_machine.states.init_client.logos_loading import LogosLoadingState
    from gui.game_loading.state_machine.states.init_client.client_loading_stub import ClientLoadingStubState

class LogosShownToClientLoadingStubTransition(SourceToSingleTargetTransition):
    __slots__ = ()

    def __init__(self, priority=0):
        super(LogosShownToClientLoadingStubTransition, self).__init__(token=GameLoadingStatesEvents.LOGOS_SHOWN.value, priority=priority)

    def _apply(self, event, source, target):
        machine = target.getMachine()
        if machine is None:
            return False
        else:
            return self._condition(machine)

    def _condition(self, machine):
        return machine.isGameLoadingComplete


class LogosShownToClientLoadingTransition(LogosShownToClientLoadingStubTransition):
    __slots__ = ()

    def _condition(self, machine):
        return not super(LogosShownToClientLoadingTransition, self)._condition(machine)


class ClientLoadingTransition(StringEventTransition):
    __slots__ = ()

    def __init__(self, priority=0):
        super(ClientLoadingTransition, self).__init__(token=GameLoadingStatesEvents.CLIENT_LOADING.value, priority=priority)
