# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/request/reactive_communication.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/request/reactive_communication.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from web.web_client_api import W2CSchema, w2c

class ReactiveCommunicationConfigWebApiMixin(object):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    @w2c(W2CSchema, 'reactive_communication_config')
    def getHermodSettings(self, cmd):
        return self.__lobbyContext.getServerSettings().getReactiveCommunicationConfig().asDict()
