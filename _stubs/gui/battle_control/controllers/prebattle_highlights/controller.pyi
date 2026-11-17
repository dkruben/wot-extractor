# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/prebattle_highlights/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import SoundGroups as SoundGroups
import typing as typing
from enum import Enum as Enum
from future.utils import viewvalues as viewvalues
import BattleReplay as BattleReplay
import BigWorld as BigWorld
import Event as Event
import Keys as Keys
import constants as constants
from account_helpers.settings_core.settings_constants import GAME as GAME, GRAPHICS as GRAPHICS
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from constants import ARENA_PERIOD as ARENA_PERIOD
from gui import InputHandler as InputHandler
from gui.battle_control.arena_info.interfaces import IArenaPeriodController as IArenaPeriodController
from gui.battle_control.arena_info.settings import ARENA_LISTENER_SCOPE as ARENA_LISTENER_SCOPE
from gui.battle_control.avatar_getter import getInputHandler as getInputHandler
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.prebattle_highlights.pbh_constants import TankSizes as TankSizes, TANK_SIZE_LOWER_BOUNDS as TANK_SIZE_LOWER_BOUNDS
from gui.battle_control.controllers.prebattle_highlights.pbh_helpers import timeUntilEndOfPeriod as timeUntilEndOfPeriod, PbhSounds as PbhSounds
from gui.battle_control.controllers.prebattle_highlights.pbh_prefab_loader import PBHPrefabLoader as PBHPrefabLoader, PrefabLoaderStatus as PrefabLoaderStatus
from gui.battle_control.controllers.prebattle_highlights.sub_systems.pbh_gamelogic_observer import PbhGameLogicObserver as PbhGameLogicObserver
from gui.battle_control.controllers.prebattle_highlights.sub_systems.pbh_sequence_handler import PbhSequenceHandler as PbhSequenceHandler, EMPTY_SEQUENCE_LAYER_VALUE as EMPTY_SEQUENCE_LAYER_VALUE
from gui.battle_control.controllers.prebattle_highlights.sub_systems.pbh_vehicle_apperance_mover import PbhVehicleAppearanceMover as PbhVehicleAppearanceMover
from gui.battle_control.controllers.prebattle_highlights.sub_systems.pbh_window_handler import PbhWindowHandler as PbhWindowHandler
from gui.battle_control.view_components import ViewComponentsController as ViewComponentsController
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gameplay import IGameplayLogic as IGameplayLogic
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from uilogging.prebattle_highlights.constants import PrebattleHighlightsLogKeys as PrebattleHighlightsLogKeys
from uilogging.prebattle_highlights.loggers import PrebattleHighlightsEventLogger as PrebattleHighlightsEventLogger, PBHViewingLogInfo as PBHViewingLogInfo
from vehicle_systems.tankStructure import selectItemByTankSize as selectItemByTankSize, getVehicleAABB as getVehicleAABB
from wg_async import wg_await as wg_await, wg_async as wg_async
from typing import Dict as Dict, Tuple as Tuple
from gui.battle_control.controllers.prebattle_highlights.sub_systems.base_sub_system import BasePbhSubSystem as BasePbhSubSystem
_logger: Any

class PbhSubSystemsNames(Enum):
    SEQUENCE_HANDLER = 'sequence_handler'
    GAME_LOGIC_OBSERVER = 'game_logic_observer'
    WINDOW_HANDLER = 'window_handler'
    VEHICLE_APPEARANCE_MOVER = 'vehicle_appearance_mover'

class PrebattleHighlightsController(IArenaPeriodController, ViewComponentsController):
    __sessionProvider: Any
    __gameplayLogic: Any
    __lobbyCtx: Any
    __settingsCore: Any
    __triggeredByDevHotkey: Any
    __displayingHighlights: Any
    __ending: Any
    __finished: Any
    __winnersStats: Any
    __pbhWasShown: Any
    __pbhSize: Any
    __meetsHistoricalCompliance: Any
    __prefabLoader: Any
    __uiLogger: Any
    onVehiclesDataReady: Any
    onStartPbhStage: Any
    __subSystems: Any
    def __init__(self):
        ...
    @property
    def sequenceHandler(self):
        ...
    @property
    def gameLogicObserver(self):
        ...
    @property
    def windowHandler(self):
        ...
    @property
    def vehicleAppearanceMover(self):
        ...
    @property
    def vehiclesData(self):
        ...
    @property
    def meetsHistoricalCompliance(self):
        ...
    @property
    def displayingHighlights(self):
        ...
    @property
    def winnersStats(self):
        ...
    @property
    def pbhWasShown(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def getCtrlScope(self):
        ...
    def getControllerID(self):
        ...
    def setWinnersStats(self, winners):
        ...
    def getPBHSize(self):
        ...
    def invalidatePeriodInfo(self, period, endTime, length, additionalInfo):
        ...
    def handleEscClose(self):
        ...
    # decorador original: @wg_async
    def __start(self):
        ...
    def __isTooLateToStart(self, period, sequenceLayerInfo):
        ...
    def __skipPrebattleHighlights(self):
        ...
    # decorador original: @wg_async
    def __end(self):
        ...
    def __finishHighlights(self):
        ...
    def __toggleHighlights(self, event):
        ...
