# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/battle_control/controllers/comp7_voip_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import Keys as Keys
import typing as typing
import CommandMapping as CommandMapping
import SoundGroups as SoundGroups
import VOIP as VOIP
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import COMP7_IS_VOIP_IN_BATTLE_ACTIVATED as COMP7_IS_VOIP_IN_BATTLE_ACTIVATED
from comp7_core.gui.battle_control.interfaces import IComp7VOIPController as IComp7VOIPController
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from constants import ARENA_PERIOD as ARENA_PERIOD, IS_CHINA as IS_CHINA, REQUEST_COOLDOWN as REQUEST_COOLDOWN, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui import g_keyEventHandlers as g_keyEventHandlers
from gui.battle_control import event_dispatcher as event_dispatcher
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.utils.key_mapping import getKey as getKey, getReadableKey as getReadableKey
from helpers import dependency as dependency
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.shared_messages import ClientActionMessage as ClientActionMessage
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from VOIP.VOIPManager import VOIPManager as VOIPManager
_logger: Any
_VOICE_CHAT_ENTER_SOUND_EVENT = 'comp_7_voicechat_enter'
_VOICE_CHAT_EXIT_SOUND_EVENT = 'comp_7_voicechat_exit'

class Comp7VOIPController(IComp7VOIPController):
    __slots__: tuple
    __sessionProvider: Any
    __messageShown: Any
    __cooldownCallback: Any
    __isTeamChannelAvailable: Any
    def __init__(self, isTeamChannelAvailable):
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
    def __VOIPManager(self):
        ...
    @property
    def __arenaBonusType(self):
        ...
    def startControl(self, *_, **__):
        ...
    def stopControl(self):
        ...
    def arenaLoadCompleted(self):
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
    def __tryShowInfoMessage(self):
        ...
    def __getMessage(self):
        ...
    def __handleKeyEvent(self, event):
        ...
    def __clearCooldown(self):
        ...
