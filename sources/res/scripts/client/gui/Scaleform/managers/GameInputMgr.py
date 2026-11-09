# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/managers/GameInputMgr.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/managers/GameInputMgr.py
from __future__ import absolute_import
import typing, Keys, CommandMapping
from Event import Event
from debug_utils import LOG_DEBUG
from gui.Scaleform.framework.entities.abstract.GameInputManagerMeta import GameInputManagerMeta
from gui.shared.utils.key_mapping import getScaleformKey
from messenger.m_constants import PROTO_TYPE
from messenger.proto import proto_getter
if typing.TYPE_CHECKING:
    from typing import Callable
_KEY_ESCAPE = getScaleformKey(Keys.KEY_ESCAPE)
_KEY_DOWN = 'keyDown'
_KEY_UP = 'keyUp'

class GameInputMgr(GameInputManagerMeta):

    def __init__(self):
        super(GameInputMgr, self).__init__()
        self.__voiceChatKey = self._getCurrentChatKey()
        self.onEscape = Event()

    @proto_getter(PROTO_TYPE.BW_CHAT2)
    def bwProto(self):
        return

    def handleGlobalKeyEvent(self, keyCode, eventType):
        LOG_DEBUG('GameInputMgr.handleGlobalKeyEvent', keyCode, eventType)
        if keyCode == self.__voiceChatKey:
            self.bwProto.voipController.setMicrophoneMute(eventType == _KEY_UP)
        if keyCode == _KEY_ESCAPE:
            self.onEscape()

    def updateChatKeyHandlers(self, value=None):
        if value and self.__voiceChatKey != value:
            self._clearChatKeyHandlers()
            if value is None:
                self.__voiceChatKey = self._getCurrentChatKey()
            else:
                self.__voiceChatKey = value
            self._setupChatKeyHandlers()
        return

    def addEscapeListener(self, listener):
        self.onEscape += listener
        if len(self.onEscape) == 1:
            self.as_addKeyHandlerS(_KEY_ESCAPE, _KEY_DOWN, True)

    def removeEscapeListener(self, listener):
        self.onEscape -= listener
        if not self.onEscape:
            self.as_clearKeyHandlerS(_KEY_ESCAPE, _KEY_DOWN)

    def _populate(self):
        super(GameInputMgr, self)._populate()
        self._setupChatKeyHandlers()

    def _dispose(self):
        self._clearChatKeyHandlers()
        super(GameInputMgr, self)._dispose()

    def _getCurrentChatKey(self):
        return getScaleformKey(CommandMapping.g_instance.get('CMD_VOICECHAT_MUTE'))

    def _setupChatKeyHandlers(self):
        self.as_addKeyHandlerS(self.__voiceChatKey, _KEY_DOWN, True, _KEY_UP)
        self.as_addKeyHandlerS(self.__voiceChatKey, _KEY_UP, False, None)
        return

    def _clearChatKeyHandlers(self):
        self.as_clearKeyHandlerS(self.__voiceChatKey, _KEY_DOWN)
        self.as_clearKeyHandlerS(self.__voiceChatKey, _KEY_UP)
