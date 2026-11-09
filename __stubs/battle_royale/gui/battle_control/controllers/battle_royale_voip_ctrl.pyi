# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/battle_control/controllers/battle_royale_voip_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import VOIP as VOIP
import CommandMapping as CommandMapping
from account_helpers.settings_core.settings_constants import SOUND as SOUND
from constants import IS_CHINA as IS_CHINA, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui import g_keyEventHandlers as g_keyEventHandlers
from gui.battle_control import event_dispatcher as event_dispatcher
from gui.battle_control.arena_info.interfaces import IBRVOIPController as IBRVOIPController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.shared.utils.key_mapping import getKey as getKey
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from VOIP.VOIPManager import VOIPManager as VOIPManager
_logger: Any

class BRVOIPController(IBRVOIPController):
    __slots__: tuple
    __sessionProvider: Any
    __settingsCore: Any
    @property
    def isVoipSupported(self):
        ...
    @property
    def isVoipEnabled(self):
        ...
    @property
    def isJoined(self):
        ...
    @property
    def isTeamVoipEnabled(self):
        ...
    @property
    def __VOIPManager(self):
        ...
    def startControl(self, *_, **__):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def arenaLoadCompleted(self):
        ...
    def toggleChannelConnection(self):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __onChannelAvailable(self, *_, **__):
        ...
    def __tryActivateVOIP(self):
        ...
    def __restoreChannelState(self):
        ...
    def __isSoloPlayer(self):
        ...
    def __handleKeyEvent(self, event):
        ...
