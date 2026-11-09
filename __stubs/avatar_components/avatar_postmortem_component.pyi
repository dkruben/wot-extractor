# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/avatar_components/avatar_postmortem_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BattleReplay as BattleReplay
from AvatarInputHandler.control_modes import PostMortemControlMode as PostMortemControlMode
from account_helpers.settings_core.settings_constants import GAME as GAME
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from helpers import dependency as dependency
from constants import POSTMORTEM_MODIFIERS as POSTMORTEM_MODIFIERS, DEFAULT_POSTMORTEM_SETTINGS as DEFAULT_POSTMORTEM_SETTINGS, RM_STATE as RM_STATE
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_TRAJECTORY_PROGRESS_DELAY = 0.1
_logger: Any

class SimulatedVehicleType(object):
    VEHICLE = 'vehicle'
    PLAYER = 'player'
    ATTACKER = 'attacker'

class AvatarPostmortemComponent(object):
    _lobbyContext: Any
    _guiSessionProvider: Any
    __deadOnReconnection: Any
    _currentGameModeSettings: Any
    __isSimpleDeathCam: Any
    @property
    def deadOnReconnection(self):
        ...
    @deadOnReconnection.setter
    def deadOnReconnection(self, value):
        ...
    def __init__(self):
        ...
    def onBecomePlayer(self):
        ...
    def handleKey(self, isDown, key, mods):
        ...
    def onBecomeNonPlayer(self):
        ...
    def isPostmortemFeatureEnabled(self, feature):
        ...
    def isPostmortemModificationActive(self, feature, constraint):
        ...
    def destroy(self):
        ...
    def getNextControlMode(self):
        ...
    def isSimpleDeathCam(self):
        ...
    def __setGameMode(self):
        ...
    def __applyPostMortemSettings(self):
        ...
    def __onSettingsSyncCompleted(self):
        ...
