# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/dog_tags_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
import Event as Event
from UIComponents import GamefaceMarkerComponent as GamefaceMarkerComponent
from AvatarInputHandler import cameras as cameras
from constants import ARENA_PERIOD as ARENA_PERIOD
from account_helpers.settings_core.settings_constants import GAME as GAME
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from dog_tags_common.player_dog_tag import PlayerDogTag as PlayerDogTag
from dog_tags_common.config.common import ComponentViewType as ComponentViewType
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gameplay import IGameplayLogic as IGameplayLogic
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any
_MARKER_VISIBLE_DISTANCE_ = 150.0
_MARKER_HEIGHT_ = 10.5
_MARKER_INTERVAL_ = 1.5
_MARKER_INITIAL_DELAY_ = 5.0

class DogTagsController(IBattleController):
    guiSessionProvider: Any
    lobbyContext: Any
    settingsCore: Any
    __arenaDP: Any
    __isEnabled: Any
    __eManager: Any
    __pendingVehicles: Any
    __dogTagGOs: Any
    __delayer: Any
    onArenaVehicleVictimDogTagUpdated: Any
    onKillerDogTagSet: Any
    onVictimDogTagSet: Any
    onKillerDogTagCheat: Any
    __isAvatarReady: Any
    def __init__(self, setup):
        ...
    def setKillerDogTag(self, killerDogTag):
        ...
    def setVictimsDogTags(self, victimsDogTags):
        ...
    def _initDogTagsInfo(self, vehicle):
        ...
    def _updateArenaVehicleVictimsDogTags(self, victimsDogTags):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def __onVehicleEnterWorld(self, vehicle):
        ...
    def __onVehicleLeaveWorld(self, vehicle):
        ...
    def _onPrebattleStateReached(self, _=None, __=None):
        ...
    def _extendDogTagInfo(self, dogTagsInfo):
        ...
    def __addDogTagMarker(self, vehicle):
        ...
    def __removeDogTagMarker(self, vehicle):
        ...
    def __onArenaPeriodChange(self, period, *_):
        ...
    def __canShowMarkers(self):
        ...
    def __clearMarkers(self):
        ...
    def __processVehicles(self):
        ...
