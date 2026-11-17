# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/maps_training_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from functools import partial as partial
import ArenaType as ArenaType
import adisp as adisp
from BattleReplay import g_replayCtrl as g_replayCtrl, CallbackDataNames as CallbackDataNames
import BigWorld as BigWorld
import Event as Event
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from constants import REQUEST_COOLDOWN as REQUEST_COOLDOWN
from gui.impl.lobby.maps_training.maps_training_client_settings import MapsTrainingClientSettings as MapsTrainingClientSettings
from gui.impl.lobby.maps_training.sound_constants import MapsTrainingSound as MapsTrainingSound
from gui.prb_control.entities.base.ctx import PrbAction as PrbAction
from helpers import dependency as dependency
from helpers import isPlayerAccount as isPlayerAccount
from items.vehicles import getVehicleClass as getVehicleClass
from maps_training_common.helpers import unpackMapsTrainingScenarios as unpackMapsTrainingScenarios, unpackMapsTrainingRewards as unpackMapsTrainingRewards
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from wotdecorators import condition as condition
from AccountCommands import isCodeValid as isCodeValid
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG, PREBATTLE_ACTION_NAME as PREBATTLE_ACTION_NAME
from items import vehicles as vehicles
from gui.shared import event_dispatcher as event_dispatcher, g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from skeletons.gui.game_control import IMapsTrainingController as IMapsTrainingController

class MapsTrainingController(IMapsTrainingController, IGlobalListener):
    lobbyContext: Any
    c11nService: Any
    sessionProvider: Any
    __itemsCache: Any
    ifEnabled: Any
    ifMapsTrainingPrbActive: Any
    _UNDEFINED_VALUE = -1
    __config: Any
    __mapGeometryID: Any
    __vehCompDescr: Any
    __team: Any
    __replayCallbacks: Any
    __replayConfigStored: Any
    __preferences: Any
    __configIsOld: Any
    __lastRequestTime: Any
    __exitSoundStateSet: Any
    onUpdated: Any
    def __init__(self):
        ...
    @property
    def isMapsTrainingEnabled(self):
        ...
    @property
    def isMapsTrainingPrbActive(self):
        ...
    @property
    def preferences(self):
        ...
    # decorador original: @ifEnabled
    # decorador original: @ifMapsTrainingPrbActive
    def showMapsTrainingQueue(self):
        ...
    # decorador original: @adisp.adisp_process
    def selectMapsTrainingMode(self):
        ...
    # decorador original: @adisp.adisp_process
    def selectRandomMode(self):
        ...
    def getSelectedMap(self):
        ...
    def setSelectedMap(self, mapName):
        ...
    def getSelectedVehicle(self):
        ...
    def _showVehicle(self):
        ...
    def _hideVehicle(self):
        ...
    def updateSelectedVehicle(self):
        ...
    def setSelectedVehicle(self, vehicleName):
        ...
    def getSelectedTeam(self):
        ...
    def setSelectedTeam(self, team):
        ...
    def isValid(self):
        ...
    def reset(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onEnter(self):
        ...
    def onExit(self):
        ...
    def onDisconnected(self):
        ...
    def onLobbyInited(self, event):
        ...
    def getConfig(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def setExitSoundState(self):
        ...
    def requestInitialDataFromServer(self, callback=None):
        ...
    def getPageCtx(self):
        ...
    def __clear(self):
        ...
    def __onSelectVehicleInHangar(self, event):
        ...
    def __processConfiguration(self, callback, code, errStr, value):
        ...
    def __parseConfiguration(self, configuration):
        ...
    def __restoreConfigFromReplay(self, config):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __onC11nVisibilityChanged(self, inCustomisation):
        ...
