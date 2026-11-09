# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/shells_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from itertools import chain as chain
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf.view.array import fillViewModelsArray as fillViewModelsArray
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.gen.view_models.views.lobby.loadout.shells.shell_model import ShellModel as ShellModel
from gui.impl.gen.view_models.views.lobby.loadout.shells.shells_model import ShellsModel as ShellsModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.hangar.presenters.loadout_presenter_base import LoadoutPresenterBase as LoadoutPresenterBase, LoadoutEntityProvider as LoadoutEntityProvider
from gui.impl.lobby.tank_setup.array_providers.shell import ShellProvider as ShellProvider
from gui.impl.lobby.tank_setup.configurations.shell import ShellTabs as ShellTabs, ShellDealPanel as ShellDealPanel
from gui.impl.lobby.tank_setup.interactors.shell import ShellInteractor as ShellInteractor
from gui.impl.lobby.tank_setup.tank_setup_helper import createShellSpecificationModel as createShellSpecificationModel, createShellMechanicsModels as createShellMechanicsModels, createShellMechanicsSubtypesModel as createShellMechanicsSubtypesModel
from gui.impl.wrappers.user_compound_price_model import BuyPriceModelBuilder as BuyPriceModelBuilder
from gui.shared import sound_helpers as sound_helpers
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_parameters import getShellsLoadSize as getShellsLoadSize
from gui.shared.items_parameters.shell_params import BASE_SHELL_PARAMETERS as BASE_SHELL_PARAMETERS, getMechanicParameters as getMechanicParameters
from gui.shared.items_parameters.shell_mechanics_helper import getShellParameters as getShellParameters
from helpers import dependency as dependency
from post_progression_common import TankSetupGroupsId as TankSetupGroupsId
from shared_utils import first as first
from skeletons.gui.game_control import IWalletController as IWalletController, IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.vehicle_modules import Shell as Shell
from gui.impl.lobby.tank_setup.interactors.base import InteractingItem as InteractingItem
_MIN_MECHANIC_PRIORITY = 1

# base nao representavel no stub: LoadoutPresenterBase[...]
class ShellsPresenter:
    __itemsCache: Any
    __wallet: Any
    __exchangeRates: Any
    _sectionName: Any
    _guiItemType: Any
    _provider: Any
    def __init__(self, interactingItem):
        ...
    def _getEvents(self):
        ...
    @property
    def isShellState(self):
        ...
    def _getDealPanel(self):
        ...
    def _onSlotAction(self, args):
        ...
    def _setHasChanges(self, autoloadEnabled=None):
        ...
    def _onSwapSlots(self, actionType, args):
        ...
    def _createProvider(self, vehInteractingItem):
        ...
    def _updateModel(self, recreate=True):
        ...
    def __updateShellItem(self, shellModels, shellModel):
        ...
    def __onShellUpdate(self, args):
        ...
    def __createShellItem(self, shell, installedShell):
        ...
    def __fillShellItemPriceModel(self, shellItemPrice, itemPriceModel):
        ...
