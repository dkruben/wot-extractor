# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/voip_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import typing as typing
import CommandMapping as CommandMapping
import Keys as Keys
import SoundGroups as SoundGroups
import VOIP as VOIP
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui import g_keyEventHandlers as g_keyEventHandlers, InputHandler as InputHandler
from gui.shared.utils.key_mapping import getKey as getKey, getReadableKey as getReadableKey
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from account_helpers.settings_core.settings_constants import SOUND as SOUND
from gui.impl import backport as backport
from gui.impl.gen import R as R
from last_stand.gui.battle_control.interfaces import ILSVOIPController as ILSVOIPController
_VOICE_CHAT_ENTER_SOUND_EVENT = 'ev_last_stand_voicechat_enter'
_VOICE_CHAT_EXIT_SOUND_EVENT = 'ev_last_stand_voicechat_exit'
_KEY_NONE_TEXT: Any

class LSVoipHelper(object):
    __slots__: tuple
    __sessionProvider: Any
    __settingsCore: Any
    __component: Any
    __isAvailable: Any
    def __init__(self, component):
        ...
    @property
    def isJoined(self):
        ...
    @property
    def isEnabled(self):
        ...
    @property
    def _voipController(self):
        ...
    def _playsound(self):
        ...
    def populate(self):
        ...
    def dispose(self):
        ...
    def __handleVoipStatusKeyEvent(self, event):
        ...
    def __handleKeyDown(self, event):
        ...
    def __handleKeyUp(self, event):
        ...
    def _updateMapping(self, *args):
        ...
    def _onSettingsChanged(self, diff):
        ...
    def toggleMute(self, isMuted):
        ...
    def toggleChannelConnection(self):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    @staticmethod
    def __getKeyBind(cmd):
        ...
    def __update(self, *_, **__):
        ...
