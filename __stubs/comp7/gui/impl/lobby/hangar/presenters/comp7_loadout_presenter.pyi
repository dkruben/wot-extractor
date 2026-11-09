# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/hangar/presenters/comp7_loadout_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.presenters.consumables_presenter import ConsumablesPresenter as ConsumablesPresenter
from gui.impl.lobby.hangar.presenters.equipments_presenter import EquipmentsPresenter as EquipmentsPresenter
from gui.impl.lobby.hangar.presenters.instructions_presenter import InstructionsPresenter as InstructionsPresenter
from gui.impl.lobby.hangar.presenters.loadout_presenter import LoadoutPresenter as LoadoutPresenter, _LoadoutStatesObserver as _LoadoutStatesObserver
from gui.impl.lobby.hangar.presenters.shells_presenter import ShellsPresenter as ShellsPresenter
from gui.impl.pub.view_component import ViewComponent as ViewComponent

class _Comp7LoadoutStatesObserver(_LoadoutStatesObserver):
    @property
    def _stateID(self):
        ...

class Comp7LoadoutPresenter(LoadoutPresenter):
    _STATES_OBSERVER = _Comp7LoadoutStatesObserver
    def _getChildComponents(self):
        ...

class Comp7ShellsPresenter(ShellsPresenter):
    @property
    def isShellState(self):
        ...
