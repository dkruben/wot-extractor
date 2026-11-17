# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/states.pyc (BYTECODE: a descompilacao falhou; sem bases, decoradores nem valores por omissao).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import typing as typing
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
from ClientSelectableCameraObject import ClientSelectableCameraObject as ClientSelectableCameraObject
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from cgf_components.pbs_components import PostBattleSystem as PostBattleSystem
from frameworks_common.state_machine import StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui import SystemMessages as SystemMessages
from gui.ClientHangarSpace import customizationHangarCFG as customizationHangarCFG
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.trainings.states import TrainingRoomState as TrainingRoomState
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.battle_results.service import g_pbsFakeData as g_pbsFakeData, PostBattleResultsStateMixin as PostBattleResultsStateMixin
from gui.battle_results.settings import PLAYER_TEAM_RESULT as PLAYER_TEAM_RESULT
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.lobby.vehicle_hub import OverviewState as OverviewState
from gui.lobby_state_machine.router import SubstateRouter as SubstateRouter
from gui.lobby_state_machine.states import SFViewLobbyState as SFViewLobbyState, LobbyState as LobbyState, SubScopeSubLayerState as SubScopeSubLayerState, LobbyStateDescription as LobbyStateDescription, UntrackedState as UntrackedState, LobbyStateFlags as LobbyStateFlags
from gui.lobby_state_machine.transitions import HijackTransition as HijackTransition
from gui.prb_control import prbDispatcherProperty as prbDispatcherProperty
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.system_factory import collectBattleResultStatsCtrl as collectBattleResultStatsCtrl
from gui.shared.utils.functions import getArenaImage as getArenaImage, getViewName as getViewName
from gui.subhangar.subhangar_observer import hangarVehicleAABB as hangarVehicleAABB, selectItemByTankSize as selectItemByTankSize
from gui.subhangar.subhangar_state_groups import SubhangarStateGroupConfigProvider as SubhangarStateGroupConfigProvider, SubhangarStateGroups as SubhangarStateGroups, SubhangarStateGroupConfig as SubhangarStateGroupConfig, CameraMover as CameraMover
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from helpers.events_handler import EventsHandler as EventsHandler
from items.components.c11n_constants import SeasonType as SeasonType
from shared_utils import first as first
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
_logger: Any
_TANK_SIZE_LOWER_BOUNDS: Any
_HIDDEN_TANK_LOCATION: Any
_SHOULD_GO_BACK_AFTER_LOADING: Any
_TAB_STATE_ID: Any
_PBS_SUBHANGAR_GROUPS_BY_SIZE: Any
PostBattleResultsEntryState: Any
_LoadingState: Any
_LoadingStateWithRetainedCamera: Any
PostBattleResultsState: Any
_OverviewTab: Any
_TeamScoreTab: Any
MissionProgressTab: Any
_FinancialReportTab: Any

# gerado do bytecode: classes base desconhecidas
class PostBattleResultsEntryProto:
    _PostBattleResultsEntryProto__hangarSpace: Any
    _PostBattleResultsEntryProto__battleResults: Any
    _PostBattleResultsEntryProto__itemsCache: Any
    _PostBattleResultsEntryProto__itemsFactory: Any
    _PostBattleResultsEntryProto__c11nService: Any
    def __init__(self, flags=...):
        ...
    def getSubhangarStateGroupConfig(self):
        ...
    def serializeParams(self):
        ...
    def goTo(cls, arenaUniqueID, bonusType, tabStateId=...):
        ...
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# gerado do bytecode: classes base desconhecidas
class LoadingProto:
    _LoadingProto__battleResults: Any
    _LoadingProto__hangarSpace: Any
    _LoadingProto__onSpaceOrVehicleChange: Any
    _LoadingProto__goToWhenAABBAvailable: Any
    _LoadingProto__onSpaceAvailable: Any
    def __init__(self, flags=...):
        ...
    def resultsState(self):
        ...
    def _getEvents(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def __onSpaceOrVehicleChange(self):
        ...
    def __goToWhenAABBAvailable(self):
        ...
    def __onSpaceAvailable(self):
        ...

# gerado do bytecode: classes base desconhecidas
class LoadingWithRetainedCameraProto:
    def getSubhangarStateGroupConfig(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

# gerado do bytecode: classes base desconhecidas
class PostBattleResultsProto:
    _PostBattleResultsProto__hangarSpace: Any
    _PostBattleResultsProto__battleResults: Any
    def __init__(self, flags=...):
        ...
    def serializeParams(self):
        ...
    def getSubhangarStateGroupConfig(self):
        ...
    def prbDispatcher(self):
        ...
    def getNavigationDescription(self):
        ...
    def getViewKey(self, params=...):
        ...
    def _getView(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _preventNavigationOutside(self, event):
        ...

# gerado do bytecode: classes base desconhecidas
class PostBattleTab:
    _PostBattleTab__hangarSpace: Any
    _PostBattleTab__onSpaceChanged: Any
    def __init__(self, flags=...):
        ...
    def loadingState(self):
        ...
    def entryState(self):
        ...
    def registerTransitions(self):
        ...
    def serializeParams(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _getEvents(self):
        ...
    def __onSpaceChanged(self):
        ...

# gerado do bytecode: classes base desconhecidas
class OverviewTabProto:
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...

# gerado do bytecode: classes base desconhecidas
class BlurredResultTab:
    def getNavigationDescription(self):
        ...
    def _onEntered(self, event):
        ...

# gerado do bytecode: classes base desconhecidas
class TeamScoreTabProto:
    ...

# gerado do bytecode: classes base desconhecidas
class MissionProgressTabProto:
    ...

# gerado do bytecode: classes base desconhecidas
class FinancialReportTabProto:
    ...

# gerado do bytecode: classes base desconhecidas
class PBSSceneSetup:
    _PBSSceneSetup__hangarSpace: Any
    def __init__(self, mapImageName):
        ...
    def moveCamera(self, cameraManager, cameraName):
        ...
    def moveCameraFailed(self):
        ...

def registerStates(lsm):
    ...
def registerTransitions(lsm):
    ...
def generatePostBattleStateClasses(parentStateCls, entryStateProto=..., loadingProto=..., loadingWithRetainedCameraProto=..., resultsProto=..., overviewProto=..., teamScoreProto=..., missionProgressProto=..., financialReportProto=...):
    ...
def shouldHijackPBSEntry(event, targetStateClass=...):
    ...
def _getVehicleCDAndOutfit(battleResultsService, arenaUniqueID):
    ...
def _moveTank(hangarConfig, position, yawPitchRoll):
    ...

def __getattr__(name: str) -> Any: ...  # stub incompleto (gerado do bytecode)
