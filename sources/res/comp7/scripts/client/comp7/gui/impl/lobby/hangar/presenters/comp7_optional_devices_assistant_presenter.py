# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/hangar/presenters/comp7_optional_devices_assistant_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/hangar/presenters/comp7_optional_devices_assistant_presenter.py
from __future__ import absolute_import
import typing
from frameworks_common.state_machine import visitor
from gui.impl.lobby.hangar.presenters.optional_devices_assistant_presenter import _OptionalDevicesObserver, OptionalDevicesAssistantPresenter
if typing.TYPE_CHECKING:
    from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine
    from frameworks_common.state_machine import State

class _Comp7OptionalDevicesObserver(_OptionalDevicesObserver):

    def isObservingState(self, state):
        from comp7.gui.impl.lobby.hangar.states import Comp7EquipmentLoadoutState
        lsm = state.getMachine()
        return visitor.isDescendantOf(state, lsm.getStateByCls(Comp7EquipmentLoadoutState)) or state.getStateID() == Comp7EquipmentLoadoutState.STATE_ID


class Comp7OptionalDevicesAssistantPresenter(OptionalDevicesAssistantPresenter):
    _STATES_OBSERVER = _Comp7OptionalDevicesObserver
