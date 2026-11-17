# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/w2gt/w2gt_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import logging as logging
import typing as typing
import ArenaType as ArenaType
import BigWorld as BigWorld
from Event import Event as Event, EventManager as EventManager
from client_request_lib.exceptions import ResponseCodes as ResponseCodes
from constants import ARENA_PERIOD as ARENA_PERIOD, ROLE_TYPE_TO_LABEL as ROLE_TYPE_TO_LABEL, ROLE_TYPE as ROLE_TYPE
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.arena_info.interfaces import IW2GTBattleController as IW2GTBattleController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.w2gt.w2gt_data_mgr import W2GTDataMgr as W2GTDataMgr, W2gtProgress as W2gtProgress
from gui.battle_control.controllers.w2gt.w2gt_plugin import W2GTPlugin as W2GTPlugin
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items.Vehicle import VEHICLE_CLASS_NAME as VEHICLE_CLASS_NAME
from helpers import dependency as dependency
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.shared_messages import ClientActionMessage as ClientActionMessage, ACTION_MESSAGE_TYPE as ACTION_MESSAGE_TYPE
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IW2GTGameController as IW2GTGameController
from wg_async import wg_async as wg_async, wg_await as wg_await
from Vehicle import Vehicle as Vehicle
from typing import Optional as Optional, Dict as Dict
from gui.game_control.w2gt_controller import _W2gtResponseData as _W2gtResponseData
_logger: Any
_NOT_MODIFIED_CODE = 304
_DEFAULT_VEHICLE_ROLE: dict

class _RequestState(enum.IntEnum):
    NONE = 1
    IN_PROGRESS = 2
    RECEIVED = 3

class W2GTBattleController(IW2GTBattleController):
    __w2gtGameCtrl: Any
    __settingsCore: Any
    __period: Any
    __periodStartTime: Any
    __playerVehicleID: Any
    __ownVehicle: Any
    __plugin: Any
    __receivedData: Any
    __arenaUniqueID: Any
    __progress: Any
    __spaceLoaded: Any
    __requestState: Any
    __isPlayerAlive: Any
    __isActive: Any
    __postponedClientMessages: Any
    __em: Any
    onStageChanged: Any
    def __init__(self):
        ...
    @property
    def isActive(self):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def isArenaSuitable(self, arena):
        ...
    def spaceLoadCompleted(self):
        ...
    def invalidateArenaInfo(self):
        ...
    def invalidateVehiclesInfo(self, arenaDP):
        ...
    def invalidateVehicleStatus(self, flags, vInfoVO, arenaDP):
        ...
    def setPeriodInfo(self, period, endTime, length, additionalInfo):
        ...
    def invalidatePeriodInfo(self, period, endTime, length, additionalInfo):
        ...
    # decorador original: @wg_async
    def __tryInitializeData(self):
        ...
    def __tryRun(self):
        ...
    def __sendClientMessages(self):
        ...
    def __onPluginStageChanged(self, stageID, ctx):
        ...
    def __onServerSettingsSyncCompleted(self):
        ...
    def __getVehicleRole(self, vehTypeDescriptor):
        ...
    def __clear(self):
        ...
