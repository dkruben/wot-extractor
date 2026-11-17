# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tank_setup/optional_devices_assistant/hangar.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers.AccountSettings import AccountSettings as AccountSettings, OptionalDevicesAssistant as OptionalDevicesAssistant
from constants import QUEUE_TYPE as QUEUE_TYPE
from gui.game_control.wot_plus.wot_plus_opt_device_assist import OptionalDevicesAssistantCtrl as OptionalDevicesAssistantCtrl
from gui.game_control.wotlda.constants import OptDeviceAssistType as OptDeviceAssistType
from gui.impl.common.base_sub_model_view import BaseSubModelView as BaseSubModelView
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_item import OptionalDevicesAssistantItem as ODAItem
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_model import OptionalDevicesAssistantStateEnum as OptionalDevicesAssistantStateEnum, OptionalDevicesAssistantItemType as OptionalDevicesAssistantItemType
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_preset import OptionalDevicesAssistantPreset as OptDeviceAssistPresetUI, OptionalDevicesAssistantModeTypeEnum as OptionalDevicesAssistantModeTypeEnum
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_preset import OptionalDevicesAssistantTypeEnum as OdaUItype
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_preset_model_type import OptionalDevicesAssistantPresetTypeEnum as PresetType
from gui.impl.gui_decorators import args2params as args2params
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from helpers import dependency as dependency
from renewable_subscription_common.optional_devices_usage_config import GenericOptionalDevice as GenericOptionalDevice
from skeletons.gui.game_control import IWotPlusController as IWotPlusController, IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.event_bus import SharedEvent as SharedEvent
from typing import List as List
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.optional_devices_assistant_model import OptionalDevicesAssistantModel as OptionalDevicesAssistantModel
from renewable_subscription_common.optional_devices_usage_config import VehicleLoadout as VehicleLoadout
_GENERIC_INT_TYPE_TO_UI_ENUM: dict

class OptionalDevicesAssistantView(BaseSubModelView):
    __slots__: tuple
    _wotPlusCtrl: Any
    _comp7onslaughtCtrl: Any
    _itemsCache: Any
    _queueType: Any
    def __init__(self, viewModel, queueType):
        ...
    @property
    def viewModel(self):
        ...
    def onLoading(self, *args, **kwargs):
        ...
    def updateVehicle(self, _=None):
        ...
    def fillModel(self):
        ...
    def showNoDataState(self):
        ...
    def showHiddenState(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _fillVehicleLoadoutsData(self, loadouts):
        ...
    def __onDataChanged(self, _):
        ...
    def __isSuitableVehicle(self, vehicle):
        ...
    def __isVehicleDataAvailable(self, vehicle):
        ...
    # decorador original: @args2params(...)
    def __onPresetSelected(self, presetType):
        ...
    def __createPreset(self, presetType, resultType, resultVehicle, loadouts):
        ...
