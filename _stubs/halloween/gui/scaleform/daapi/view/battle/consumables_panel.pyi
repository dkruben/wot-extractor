# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/consumables_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import logging as logging
from datetime import datetime as datetime
from functools import partial as partial
import BigWorld as BigWorld
from helpers import dependency as dependency
from gui import TANKMEN_ROLES_ORDER_DICT as TANKMEN_ROLES_ORDER_DICT
from halloween.gui.scaleform.daapi.view.meta.ConsumablesPanelMeta import ConsumablesPanelMeta as ConsumablesPanelMeta
from halloween.gui.halloween_account_settings import getSettings as getSettings, AccountSettingsKeys as AccountSettingsKeys
from constants import EQUIPMENT_STAGES as EQUIPMENT_STAGES, ARENA_PERIOD as ARENA_PERIOD
from gui.Scaleform.genConsts.CONSUMABLES_PANEL_SETTINGS import CONSUMABLES_PANEL_SETTINGS as CONSUMABLES_PANEL_SETTINGS
from halloween_common import halloween_constants as halloween_constants
from halloween.gui.halloween_gui_constants import AmmoPanelSwitchPreset as AmmoPanelSwitchPreset
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.battle.shared.consumables_panel import TOOLTIP_FORMAT as TOOLTIP_FORMAT, EMPTY_EQUIPMENT_TOOLTIP as EMPTY_EQUIPMENT_TOOLTIP
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, VEHICLE_DEVICE_IN_COMPLEX_ITEM as VEHICLE_DEVICE_IN_COMPLEX_ITEM, DEVICE_STATE_AS_DAMAGE as DEVICE_STATE_AS_DAMAGE, DEVICE_STATE_CRITICAL as DEVICE_STATE_CRITICAL, DEVICE_STATE_DESTROYED as DEVICE_STATE_DESTROYED
from gui.battle_control.controllers.consumables.equipment_ctrl import NeedEntitySelection as NeedEntitySelection, IgnoreEntitySelection as IgnoreEntitySelection
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from builtins import range as range
_logger: Any
R_ICON_HUD = R.images.gui.maps.icons.artefact.hud
R_TEXT = R.strings.artefacts
_ACTIVE_EQUIPMENT_STAGES: tuple
_PRESETS_CUSTOM_INDEXES: dict

class HWConsumablesPanel(ConsumablesPanelMeta):
    guiSessionProvider: Any
    _HW_EQUIPMENT_START_IDX = None
    _HW_EQUIPMENT_END_IDX = None
    _EQUIPMENT_START_IDX = 0
    _EQUIPMENT_END_IDX = 2
    _ORDERS_START_IDX = 6
    _ORDERS_END_IDX = 7
    _OPT_DEVICE_START_IDX = 8
    _OPT_DEVICE_END_IDX = 10
    PERMANENT_GLOW_MIN_DURATION_SECONDS = 7.0
    HW_EQUIPMENT_UPDATE_INTERVAL = 0.1
    HW_EQUIPMENTS_NOT_IN_PANEL: list
    _permanentGlows: Any
    _permanentGlowTimestamp: Any
    _arenaPeriod: Any
    _hwEquipmentGlow: Any
    _hwEquipmentGlowAllowed: Any
    _callbackDelayer: Any
    _shellsCount: Any
    _nitroIntCD: Any
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
    def _addHWEquipmentSlot(self, idx, intCD, item):
        ...
    def _getEquipmentIcon(self, idx, item, icon):
        ...
    def _updateHWEquipmentKeyHandlers(self, updateSlots=None):
        ...
    def _onMappingChanged(self, *args):
        ...
    def _handleEquipmentPressed(self, intCD, entityName=None, idx=None):
        ...
    def _updateEquipmentGlow(self, idx, item):
        ...
    def _updateEquipmentSlot(self, idx, item, forceUpdate=False):
        ...
    def _showHWEquipmentGlow(self, idx, glowID):
        ...
    def _onCurrentShellChanged(self, intCD):
        ...
    def _onArenaPeriodChange(self, period, periodEndTime, periodLength, periodAdditionalInfo):
        ...
    def _onUpdateHWEquipmentTimer(self):
        ...
    def _onUpdateHWEquipment(self, onModifier=False):
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
    def _isHalloweenEquipment(item):
        ...
    @staticmethod
    def _isNitroEquipment(item):
        ...
    @classmethod
    def _isHalloweenEmptySlot(cls, item):
        ...
    @classmethod
    def _isHalloweenPassive(cls, item):
        ...
    @staticmethod
    def _isSuperShell(item):
        ...
    @staticmethod
    def _hasUsageCost(item):
        ...
    @classmethod
    def _hasDuration(cls, item):
        ...
    def _onEquipmentCooldownInPercent(self, key, percent):
        ...
    def _onEquipmentCooldownTime(self, key, timeLeft, isBaseTime, isFlash):
        ...
    def _onUpdateVehicleModifiers(self, _):
        ...
