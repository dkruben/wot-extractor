# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/loadout_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.presenters.consumables_presenter import ConsumablesPresenter as ConsumablesPresenter
from gui.impl.lobby.hangar.presenters.equipments_presenter import EquipmentsPresenter as EquipmentsPresenter
from gui.impl.lobby.hangar.presenters.instructions_presenter import InstructionsPresenter as InstructionsPresenter
from gui.impl.lobby.hangar.presenters.loadout_presenter import LoadoutPresenter as LoadoutPresenter, _LoadoutStatesObserver as _LoadoutStatesObserver
from gui.impl.lobby.hangar.presenters.loadout_presenter_base import LoadoutEntityProvider as LoadoutEntityProvider
from gui.impl.lobby.hangar.presenters.shells_presenter import ShellsPresenter as ShellsPresenter
from gui.impl.lobby.tank_setup.configurations.consumable import ConsumableTabs as ConsumableTabs
from gui.impl.lobby.tank_setup.interactors.consumable import ConsumableInteractor as ConsumableInteractor
from fort_rush.gui.impl.lobby.tank_setup.array_provider import FortRushConsumableProvider as FortRushConsumableProvider
from gui.impl.gen.view_models.views.lobby.loadout.panel.ammunition.ammunition_panel_model import AmmunitionPanelModel as AmmunitionPanelModel

class _FortRushLoadoutStatesObserver(_LoadoutStatesObserver):
    @property
    def _stateID(self):
        ...

class FortRushLoadoutPresenter(LoadoutPresenter):
    _VIEW_MODEL = AmmunitionPanelModel
    _STATES_OBSERVER = _FortRushLoadoutStatesObserver
    def _getChildComponents(self):
        ...

class FortRushConsumablesPresenter(ConsumablesPresenter):
    _provider: Any
    def _createProvider(self, vehInteractingItem):
        ...

class FortRushShellsPresenter(ShellsPresenter):
    @property
    def isShellState(self):
        ...
