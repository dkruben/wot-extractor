# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/consumables_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import lrange as lrange
import time as time
import logging as logging
from datetime import datetime as datetime
from functools import partial as partial
from math import ceil as ceil
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from gui import TANKMEN_ROLES_ORDER_DICT as TANKMEN_ROLES_ORDER_DICT
from last_stand.gui.scaleform.daapi.view.meta.ConsumablesPanelMeta import ConsumablesPanelMeta as ConsumablesPanelMeta
from last_stand.gui.ls_account_settings import getSettings as getSettings, AccountSettingsKeys as AccountSettingsKeys
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES, ARENA_PERIOD as ARENA_PERIOD
from gui.Scaleform.genConsts.CONSUMABLES_PANEL_SETTINGS import CONSUMABLES_PANEL_SETTINGS as CONSUMABLES_PANEL_SETTINGS
from last_stand.gui.ls_gui_constants import AmmoPanelSwitchPreset as AmmoPanelSwitchPreset
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.battle.shared.consumables_panel import TOOLTIP_FORMAT as TOOLTIP_FORMAT, EMPTY_EQUIPMENT_TOOLTIP as EMPTY_EQUIPMENT_TOOLTIP
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, VEHICLE_DEVICE_IN_COMPLEX_ITEM as VEHICLE_DEVICE_IN_COMPLEX_ITEM, DEVICE_STATE_AS_DAMAGE as DEVICE_STATE_AS_DAMAGE, DEVICE_STATE_CRITICAL as DEVICE_STATE_CRITICAL, DEVICE_STATE_DESTROYED as DEVICE_STATE_DESTROYED
from gui.battle_control.controllers.consumables.equipment_ctrl import NeedEntitySelection as NeedEntitySelection, IgnoreEntitySelection as IgnoreEntitySelection
from last_stand_common.last_stand_constants import BOOSTER_FACTOR_NAMES as BOOSTER_FACTOR_NAMES
from last_stand_common.ls_utils.boosters import getVehicleBoosterFactorsComponent as getVehicleBoosterFactorsComponent
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control import avatar_getter as avatar_getter
_logger: Any
R_ICON_HUD = R.images.gui.maps.icons.artefact.hud
R_TEXT = R.strings.artefacts
_ACTIVE_EQUIPMENT_STAGES: tuple
_PRESETS_CUSTOM_INDEXES: dict

class LSConsumablesPanel(ConsumablesPanelMeta):
    _LS_EQUIPMENT_START_IDX = None
    _LS_EQUIPMENT_END_IDX = None
    _EQUIPMENT_START_IDX = 0
    _EQUIPMENT_END_IDX = 2
    _ORDERS_START_IDX = 6
    _ORDERS_END_IDX = 7
    _OPT_DEVICE_START_IDX = 8
    _OPT_DEVICE_END_IDX = 10
    PERMANENT_GLOW_MIN_DURATION_SECONDS = 7.0
    LS_EQUIPMENT_UPDATE_INTERVAL = 0.1
    LS_EQUIPMENTS_NOT_IN_PANEL: list
    LS_BOOSTER_FACTORS: set
    _permanentGlows: Any
    _permanentGlowTimestamp: Any
    _arenaPeriod: Any
    _lsEquipmentGlow: Any
    _lsEquipmentGlowAllowed: Any
    _callbackDelayer: Any
    _shellsCount: Any
    _lsEquipmentDataCache: Any
    _mask: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    @classmethod
    def _initIndexes(cls):
        ...
    def _dispose(self):
        ...
    def _updateFactors(self, diff):
        ...
    def _resetCds(self):
        ...
    def _reset(self):
        ...
    def _generateEquipmentKey(self, idx, item):
        ...
    def _onShellsAdded(self, intCD, descriptor, quantity, _, gunSettings, isInfinite):
        ...
    def _onShellsUpdated(self, intCD, quantity, *args):
        ...
    def _updateShellGlow(self, intCD, quantity, prevQuantity=None):
        ...
    def _onEquipmentAdded(self, intCD, item):
        ...
    def _onEquipmentUpdated(self, intCD, item):
        ...
    def _onOptionalDeviceAdded(self, optDeviceInBattle):
        ...
    def _addLSEquipmentSlot(self, idx, intCD, item):
        ...
    def _getEquipmentIcon(self, idx, item, icon):
        ...
    def _updateLSEquipmentKeyHandlers(self, updateSlots=None):
        ...
    def _onMappingChanged(self, *args):
        ...
    def _handleEquipmentPressed(self, intCD, entityName=None, idx=None):
        ...
    def _updateEquipmentGlow(self, idx, item):
        ...
    def _updateEquipmentSlot(self, idx, item, forceUpdate=False):
        ...
    def _showLSEquipmentGlow(self, idx, glowID):
        ...
    def _onCurrentShellChanged(self, intCD):
        ...
    def _onArenaPeriodChange(self, period, periodEndTime, periodLength, periodAdditionalInfo):
        ...
    def _onUpdateLSEquipmentTimer(self):
        ...
    def _clearAllEquipmentGlow(self):
        ...
    def _buildEquipmentSlotTooltipText(self, item):
        ...
    def _onVehicleStateUpdated(self, state, value):
        ...
    def _showPermanentGlow(self, idx, glowID=...):
        ...
    def _hidePermanentGlow(self, idx):
        ...
    def _defferPermanentGlowChange(self, idx, glowMinDuration):
        ...
    def _isPermamentGlowShown(self, idx):
        ...
    def _isGlowShown(self, idx):
        ...
    def _clearEquipmentGlow(self, equipmentIndex, cancelCallback=True):
        ...
    def _isGlowAllowed(self, equipment):
        ...
    def _isAnyEquipmentModuleInState(self, equipment, checkDeviceStates):
        ...
    def _replaceEquipmentKeyHandler(self, keysContainer, intCD, deviceName):
        ...
    def _bookNextSlotIdx(self, startIdx, endIdx):
        ...
    @staticmethod
    def _isLSEquipment(item):
        ...
    @classmethod
    def _isLSEmptySlot(cls, item):
        ...
    @classmethod
    def _isLSPassive(cls, item):
        ...
    @classmethod
    def _isLSSituational(cls, item):
        ...
    @staticmethod
    def _isSuperShell(item):
        ...
    @staticmethod
    def _hasUsageCost(item):
        ...
    def _getUsageCost(self, intCD, variant, useCache=True):
        ...
    def _getDurationSeconds(self, intCD, variant, useCache=True):
        ...
    @classmethod
    def _hasDuration(cls, item):
        ...
