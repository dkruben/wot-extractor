# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/proto/bw/ChatActionsListener.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/bw/ChatActionsListener.py
from __future__ import absolute_import
from ChatManager import chatManager
from debug_utils import LOG_ERROR

class ChatActionsListener(object):

    def __init__(self, responseHandlers=None):
        super(ChatActionsListener, self).__init__()
        if responseHandlers is not None:
            self._responseHandlers = responseHandlers
        else:
            self._responseHandlers = {}
        return

    def addListener(self, callback, action, cid=None):
        chatManager.subscribeChatAction(callback, action, cid)

    def removeListener(self, callback, action, cid=None):
        chatManager.unsubscribeChatAction(callback, action, cid)

    def removeAllListeners(self):
        chatManager.unsubcribeAllChatActions()

    def handleChatActionFailureEvent(self, actionResponse, chatAction):
        handler = self._responseHandlers.get(actionResponse)
        if handler is None:
            return False
        else:
            if hasattr(self, handler):
                return getattr(self, handler)(actionResponse, chatAction)
            LOG_ERROR('handleChatActionFailureEvent: response handler for response %s(%s) not registered' % (
             actionResponse, actionResponse.index()))
            return False
