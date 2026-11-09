# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/battle_control/controllers/voip_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import typing as typing
import CommandMapping as CommandMapping
import Keys as Keys
import VOIP as VOIP
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.utils.key_mapping import getKey as getKey
from last_stand.gui import ls_account_settings as ls_account_settings
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys
from last_stand.gui.battle_control.interfaces import ILSVOIPController as ILSVOIPController
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from constants import IS_CHINA as IS_CHINA, REQUEST_COOLDOWN as REQUEST_COOLDOWN, ARENA_PERIOD as ARENA_PERIOD, ARENA_BONUS_TYPE_IDS as ARENA_BONUS_TYPE_IDS
from gui.battle_control import event_dispatcher as event_dispatcher
from helpers import dependency as dependency
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.shared_messages import ClientActionMessage as ClientActionMessage, ACTION_MESSAGE_TYPE as ACTION_MESSAGE_TYPE
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from VOIP.VOIPManager import VOIPManager as VOIPManager
_logger: Any

class LSVOIPController(ILSVOIPController):
    __slots__: tuple
    __sessionProvider: Any
    __messageShown: Any
    __cooldownCallback: Any
    __isTeamChannelAvailable: Any
    def __init__(self, isTeamChannelAvailable=True):
        ...
    def getControllerID(self):
        ...
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
    def isTeamChannelAvailable(self):
        ...
    @property
    def voipManager(self):
        ...
    def startControl(self, *_):
        ...
    def stopControl(self):
        ...
    def arenaLoadCompleted(self):
        ...
    def toggleMute(self, isMuted):
        ...
    def toggleChannelConnection(self, automatic=False):
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
    def __clearCooldown(self):
        ...
    def __isPlayerInSquad(self):
        ...
    def __processInfoMessages(self):
        ...
    def __tryShowInfoMessages(self):
        ...
