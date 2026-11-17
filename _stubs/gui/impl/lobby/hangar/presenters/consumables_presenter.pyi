# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/consumables_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import SoundGroups as SoundGroups
from gui.impl.gen.view_models.views.lobby.loadout.consumables.consumables_model import ConsumablesModel as ConsumablesModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel as BaseSetupModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_constants import TankSetupConstants as TankSetupConstants
from gui.impl.lobby.hangar.presenters.loadout_presenter_base import LoadoutPresenterBase as LoadoutPresenterBase, LoadoutEntityProvider as LoadoutEntityProvider
from gui.impl.lobby.tank_setup.array_providers.base import BaseVehSectionContext as BaseVehSectionContext
from gui.impl.lobby.tank_setup.array_providers.consumable import ConsumableDeviceProvider as ConsumableDeviceProvider
from gui.impl.lobby.tank_setup.configurations.consumable import ConsumableTabs as ConsumableTabs
from gui.impl.lobby.tank_setup.interactors.consumable import ConsumableInteractor as ConsumableInteractor
from gui.impl.lobby.tank_setup.tank_setup_sounds import TankSetupSoundEvents as TankSetupSoundEvents
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController
from gui.impl.lobby.tank_setup.interactors.base import InteractingItem as InteractingItem

# base nao representavel no stub: LoadoutPresenterBase[...]
class ConsumablesPresenter:
    __wallet: Any
    _sectionName: Any
    _guiItemType: Any
    _provider: Any
    def __init__(self, interactingItem):
        ...
    def createSlotActions(self):
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
    def __onAdd(self, args):
        ...
