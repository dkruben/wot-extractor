# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/frontline_loadout_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen import R as R
from gui.impl.lobby.hangar.presenters.consumables_presenter import ConsumablesPresenter as ConsumablesPresenter
from gui.impl.lobby.hangar.presenters.equipments_presenter import EquipmentsPresenter as EquipmentsPresenter
from gui.impl.lobby.hangar.presenters.instructions_presenter import InstructionsPresenter as InstructionsPresenter
from frontline.gui.impl.lobby.presenters.frontline_ability_presenter import FrontlineAbilityPresenter as FrontlineAbilityPresenter
from gui.impl.lobby.hangar.presenters.loadout_presenter import LoadoutPresenter as LoadoutPresenter, _LoadoutStatesObserver as _LoadoutStatesObserver
from gui.impl.lobby.hangar.presenters.shells_presenter import ShellsPresenter as ShellsPresenter
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineConst as FrontlineConst
from frontline.gui.impl.lobby.presenters.fl_hangar_ammunition_groups_controller import FLHangarAmmunitionGroupsController as FLHangarAmmunitionGroupsController
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from gui.impl.pub.view_component import ViewComponent as ViewComponent

class _FrontlineLoadoutStatesObserver(_LoadoutStatesObserver):
    @property
    def _stateID(self):
        ...

class FrontlineLoadoutPresenter(LoadoutPresenter):
    _STATES_OBSERVER = _FrontlineLoadoutStatesObserver
    _appLoader: Any
    _toolTipMgr: Any
    def __init__(self):
        ...
    def createToolTip(self, event):
        ...
    def _getChildComponents(self):
        ...
    def _createAmmunitionGroupsController(self, vehicle):
        ...

class FrontlineShellsPresenter(ShellsPresenter):
    @property
    def isShellState(self):
        ...
