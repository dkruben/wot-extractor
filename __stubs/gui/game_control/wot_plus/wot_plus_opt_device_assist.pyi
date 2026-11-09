# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/wot_plus/wot_plus_opt_device_assist.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
from functools import partial as partial
import typing as typing
from account_helpers.optional_devices_assistant_config import readOptionalDevicesUsageFallbackConfig as readOptionalDevicesUsageFallbackConfig, readOptionalDevicesUsageConfig as readOptionalDevicesUsageConfig, _USAGE_CONFIG_FILE as _USAGE_CONFIG_FILE, _USAGE_CONFIG_FILE_LEGENDARY as _USAGE_CONFIG_FILE_LEGENDARY
from constants import OPTIONAL_DEVICES_USAGE_CONFIG as OPTIONAL_DEVICES_USAGE_CONFIG, PREBATTLE_TYPE as PREBATTLE_TYPE
from gui.game_control.wotlda.cache import EquipmentForSubscribersCache as EquipmentForSubscribersCache
from gui.game_control.wotlda.constants import SupportedWotldaLoadoutType as SupportedWotldaLoadoutType, OptDeviceAssistType as OptDeviceAssistType, SupportedWTRRange as SupportedWTRRange
from gui.game_control.wotlda.loadout_model import vehicleOptDeviceLoadoutsSchema as vehicleOptDeviceLoadoutsSchema
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_bus import SharedEvent as SharedEvent
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from renewable_subscription_common.optional_devices_usage_config import GenericOptionalDevice as GenericOptionalDevice, VehicleLevelClassRoleGroup as VehicleLevelClassRoleGroup, VehicleLoadout as VehicleLoadout, convertServerDiffToRichTypes as convertServerDiffToRichTypes, GENERIC_OPTIONAL_DEVICE_MAP_TO_EQUIPMENT_NAME as GENERIC_OPTIONAL_DEVICE_MAP_TO_EQUIPMENT_NAME
from renewable_subscription_common.settings_constants import OptionalDevicesUsageConst as OptionalDevicesUsageConst
from skeletons.gui.game_control import IPlatoonController as IPlatoonController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Dict as Dict, Tuple as Tuple, List as List, Any as Any, Callable as Callable, Set as Set, Optional as Optional, Union as Union
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
_OptDevicePreset: _Any
_logger: _Any

class _IOptDeviceAssistDataProvider(object):
    def getPresets(self, vehicle):
        ...
    def hasLoadout(self, vehicle):
        ...

class _OptDevicesAssistLocalDataProvider(_IOptDeviceAssistDataProvider):
    _lobbyContext: _Any
    _itemsCache: _Any
    _wotPlusController: _Any
    __initialized: _Any
    _removedVehicles: _Any
    _updatedEquipmentUsages: _Any
    _vehicleToVehicleMap: _Any
    _typeToVehicleMap: _Any
    _clientEquipmentUsages: _Any
    _clientEquipmentUsagesLegendary: _Any
    __dataChangeEvent: _Any
    def __init__(self, evt):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def destroy(self):
        ...
    def getPresets(self, vehicle):
        ...
    def getMostPopularLoadout(self, vehicle):
        ...
    def _searchVehicleLoadoutsInCache(self, vehicle):
        ...
    def _searchVehicleLoadoutsInCacheLegendary(self, vehicle):
        ...
    def _syncServerSettings(self, serverDiff):
        ...
    def _onServerSettingsChange(self, diff):
        ...
    def _getOptionalDevicesFromCache(self, vehCompDescr):
        ...
    def _getOptionalDevicesFromCacheLegendary(self, vehCompDescr):
        ...
    def _checkOptionalDevicesCompatibilityWithVehicle(self, vehicleLoadouts, vehicle):
        ...

class _RemoteDataProvider(_IOptDeviceAssistDataProvider):
    _initiated: _Any
    _cache: _Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self, withDelete=False):
        ...
    def destroy(self):
        ...
    def deleteCacheFile(self):
        ...
    @property
    def clientCacheUpdatedAt(self):
        ...
    @property
    def initiated(self):
        ...
    def fillPresets(self, loadouts):
        ...
    def getPresetByLoadoutType(self, loadoutType, vehicle):
        ...
    def _generateEmptyPreset(self, vehicleCD):
        ...
    def _getRawPreset(self, loadoutType, vehicleCD):
        ...
    def _onCacheRead(self):
        ...

class OptionalDevicesAssistantCtrl(object):
    OPT_DEVICE_ASSIST_DATA_CHANGED = 'optDeviceAssistDataChanged'
    _platoonCtrl: _Any
    _wotPlusCtrl: _Any
    _SUPPORTED_PREBATTLE_TYPES: set
    _PREBATTLE_TYPES_TO_LOADOUT_TYPE: dict
    _localDataProvider: _Any
    _remoteDataProvider: _Any
    def __init__(self):
        ...
    @classmethod
    def addSupportedBattleType(cls, battleType, loadoutType):
        ...
    @property
    def remoteClientCacheUpdatedAt(self):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def heatCache(self):
        ...
    def destroy(self):
        ...
    def deleteClientCacheFile(self):
        ...
    def fillRemotePresets(self, presets):
        ...
    def getMostPopularLoadout(self, vehicle):
        ...
    def getPopularOptDevicesPresets(self, vehicle):
        ...
    def _sortOptDevicesPresets(self, vehicle, common, legendary):
        ...
    def vehicleHasLoadout(self, vehicle):
        ...
    def __isDataRetrievingAllowed(self):
        ...
    def __onOptDevAssistLocalDataChanged(self):
        ...

def _sortDevices(vehicle, loadout):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _sortComparator(categories, device, itemsCache=None):
    ...
