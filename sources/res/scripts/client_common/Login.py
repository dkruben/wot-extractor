# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client_common/Login.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client_common/Login.py
from __future__ import absolute_import
import BigWorld
from PlayerEvents import g_playerEvents
from debug_utils import LOG_DEBUG

class PlayerLogin(BigWorld.Entity):

    def __init__(self):
        pass

    def onBecomePlayer(self):
        pass

    def onBecomeNonPlayer(self):
        pass

    def onKickedFromServer(self, checkoutPeripheryID):
        LOG_DEBUG('onKickedFromServer', checkoutPeripheryID)
        g_playerEvents.onKickWhileLoginReceived(checkoutPeripheryID)

    def receiveLoginQueueNumber(self, queueNumber):
        LOG_DEBUG('receiveLoginQueueNumber', queueNumber)
        g_playerEvents.onLoginQueueNumberReceived(queueNumber)

    def handleKeyEvent(self, event):
        return False

    def setPeripheryRoutingGroup(self, peripheryRoutingGroup, availableHosts):
        g_playerEvents.onPeripheryRoutingGroupReceived(peripheryRoutingGroup, availableHosts)


Login = PlayerLogin
