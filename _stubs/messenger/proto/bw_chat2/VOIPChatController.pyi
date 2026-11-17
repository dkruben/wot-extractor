# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw_chat2/VOIPChatController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import BattleReplay as BattleReplay
import VOIP as VOIP
import CommandMapping as CommandMapping
from VOIP.voip_constants import VOIP_SUPPORTED_API as VOIP_SUPPORTED_API
from constants import ARENA_BONUS_TYPE_IDS as ARENA_BONUS_TYPE_IDS
from debug_utils import LOG_WARNING as LOG_WARNING
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from gui.shared.utils.key_mapping import getReadableKey as getReadableKey
from helpers import dependency as dependency
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.interfaces import IVOIPChatController as IVOIPChatController
from account_helpers.settings_core.settings_constants import SOUND as SOUND
from messenger.proto.shared_messages import ACTION_MESSAGE_TYPE as ACTION_MESSAGE_TYPE, ClientActionMessage as ClientActionMessage
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

class VOIPChatController(IVOIPChatController):
    __slots__: tuple
    settingsCore: Any
    __callbacks: Any
    __captureDevicesCallbacks: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def isReady(self):
        ...
    def isPlayerSpeaking(self, accountDBID):
        ...
    def isVOIPEnabled(self):
        ...
    def isVivox(self):
        ...
    def invalidateInitialization(self):
        ...
    def setMicrophoneMute(self, isMuted, force=False):
        ...
    def invalidateMicrophoneMute(self):
        ...
    # decorador original: @adisp_async
    def requestCaptureDevices(self, firstTime=False, callback=None):
        ...
    def isCurrentChannelEnabled(self):
        ...
    def enableCurrentChannel(self, enabled):
        ...
    # decorador original: @adisp_process
    def __initialize(self):
        ...
    # decorador original: @adisp_async
    def __initializeSettings(self, domain, server, livekitServer, callback):
        ...
    def __applyUserSettings(self):
        ...
    def __initResponse(self, _):
        ...
    def __failedResponse(self):
        ...
    def __captureDevicesResponse(self):
        ...
    def __onCaptureDeviceSet(self, deviceName, success):
        ...
    def __onPlayerSpeaking(self, accountDBID, isSpeak):
        ...
    def __onJoinedChannel(self, channel, isTestChannel, isRejoin):
        ...
    def __onLeftChannel(self, channel, wasTestChannel):
        ...
    def __onToggleChannelEnabled(self, event):
        ...
    @staticmethod
    def __showMessage(enable, arenaBonusType):
        ...
