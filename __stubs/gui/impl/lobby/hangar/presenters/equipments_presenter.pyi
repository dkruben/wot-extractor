# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/equipments_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import typing as typing
import SoundGroups as SoundGroups
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.loadout.equipments.equipments_model import EquipmentsModel as EquipmentsModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.hangar.presenters.loadout_presenter_base import LoadoutPresenterBase as LoadoutPresenterBase, LoadoutEntityProvider as LoadoutEntityProvider
from gui.impl.lobby.tank_setup.array_providers.base import BaseVehSectionContext as BaseVehSectionContext
from gui.impl.lobby.tank_setup.array_providers.opt_device import SimpleOptDeviceProvider as SimpleOptDeviceProvider, TrophyOptDeviceProvider as TrophyOptDeviceProvider, ModernisedOptDeviceProvider as ModernisedOptDeviceProvider, DeluxeOptDeviceProvider as DeluxeOptDeviceProvider
from gui.impl.lobby.tank_setup.configurations.opt_device import OptDeviceTabs as OptDeviceTabs
from gui.impl.lobby.tank_setup.interactors.opt_device import OptDeviceInteractor as OptDeviceInteractor
from gui.impl.lobby.tank_setup.tank_setup_sounds import TankSetupSoundEvents as TankSetupSoundEvents
from gui.impl.lobby.tank_setup.tooltips.setup_tab_tooltip_view import SetupTabTooltipView as SetupTabTooltipView
from gui.shared.event_dispatcher import showDeconstructionDeviceWindow as showDeconstructionDeviceWindow
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController, IWotPlusController as IWotPlusController
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.impl.lobby.tank_setup.interactors.base import InteractingItem as InteractingItem

# base nao representavel no stub: LoadoutPresenterBase[...]
class EquipmentsPresenter:
    __itemsCache: Any
    __wallet: Any
    __wotPlusCtrl: Any
    _sectionName: Any
    _guiItemType: Any
    _provider: Any
    def __init__(self, interactingItem):
        ...
    def createSlotActions(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _getEvents(self):
        ...
    def _createProvider(self, vehInteractingItem):
        ...
    def _getCallbacks(self):
        ...
    def _updateModel(self, recreate=True):
        ...
    def _onRevertItem(self, args):
        ...
    def __onGetMoreCurrency(self):
        ...
    def __onWotPlusStatusChanged(self, _):
        ...
    # decorador original: @wg_async
    def __onDemountItem(self, args, isDestroy=False, everywhere=True):
        ...
    # decorador original: @wg_async
    def __onUpgradeItem(self, args):
        ...
    def __onDeconstructed(self, deconstructedItemsOnVehicle, upgradItemPair):
        ...
