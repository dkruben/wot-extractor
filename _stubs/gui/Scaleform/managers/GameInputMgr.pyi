# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/managers/GameInputMgr.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import Keys as Keys
import CommandMapping as CommandMapping
from Event import Event as Event
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.Scaleform.framework.entities.abstract.GameInputManagerMeta import GameInputManagerMeta as GameInputManagerMeta
from gui.shared.utils.key_mapping import getScaleformKey as getScaleformKey
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from typing import Callable as Callable
_KEY_ESCAPE: Any
_KEY_DOWN = 'keyDown'
_KEY_UP = 'keyUp'

class GameInputMgr(GameInputManagerMeta):
    __voiceChatKey: Any
    onEscape: Any
    def __init__(self):
        ...
    # decorador original: @proto_getter(...)
    def bwProto(self):
        ...
    def handleGlobalKeyEvent(self, keyCode, eventType):
        ...
    def updateChatKeyHandlers(self, value=None):
        ...
    def addEscapeListener(self, listener):
        ...
    def removeEscapeListener(self, listener):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getCurrentChatKey(self):
        ...
    def _setupChatKeyHandlers(self):
        ...
    def _clearChatKeyHandlers(self):
        ...
