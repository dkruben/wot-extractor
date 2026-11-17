# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/hangar/presenters/comp7_optional_devices_assistant_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks_common.state_machine import visitor as visitor
from gui.impl.lobby.hangar.presenters.optional_devices_assistant_presenter import _OptionalDevicesObserver as _OptionalDevicesObserver, OptionalDevicesAssistantPresenter as OptionalDevicesAssistantPresenter
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from frameworks_common.state_machine import State as State

class _Comp7OptionalDevicesObserver(_OptionalDevicesObserver):
    def isObservingState(self, state):
        ...

class Comp7OptionalDevicesAssistantPresenter(OptionalDevicesAssistantPresenter):
    _STATES_OBSERVER = _Comp7OptionalDevicesObserver
