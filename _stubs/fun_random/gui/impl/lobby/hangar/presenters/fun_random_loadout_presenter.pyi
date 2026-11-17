# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_loadout_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher as FunSubModesWatcher
from fun_random.gui.impl.lobby.hangar.controllers.fun_random_ammo_groups_controller import FunRandomHangarAmmunitionGroupsController as FunRandomHangarAmmunitionGroupsController
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.presenters.consumables_presenter import ConsumablesPresenter as ConsumablesPresenter
from gui.impl.lobby.hangar.presenters.equipments_presenter import EquipmentsPresenter as EquipmentsPresenter
from gui.impl.lobby.hangar.presenters.instructions_presenter import InstructionsPresenter as InstructionsPresenter
from gui.impl.lobby.hangar.presenters.loadout_presenter import LoadoutPresenter as LoadoutPresenter, _LoadoutStatesObserver as _LoadoutStatesObserver
from gui.impl.lobby.hangar.presenters.shells_presenter import ShellsPresenter as ShellsPresenter
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.pub.view_component import ViewComponent as ViewComponent

class _FunRandomLoadoutStatesObserver(_LoadoutStatesObserver):
    @property
    def _stateID(self):
        ...

class FunRandomLoadoutPresenter(LoadoutPresenter, FunSubModesWatcher):
    _STATES_OBSERVER = _FunRandomLoadoutStatesObserver
    def _getChildComponents(self):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def _createAmmunitionGroupsController(self, vehicle):
        ...
    def __onSubModeChanged(self, *_):
        ...

class FunRandomShellsPresenter(ShellsPresenter):
    @property
    def isShellState(self):
        ...
