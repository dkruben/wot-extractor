# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/client_web_api/reactive_comm/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/reactive_comm/__init__.py
from __future__ import absolute_import
from helpers import dependency
from skeletons.gui.game_control import IReactiveCommunicationService
from web.client_web_api.api import C2WHandler, c2w

class ReactiveCommunicationEventHandler(C2WHandler):
    __service = dependency.descriptor(IReactiveCommunicationService)

    @property
    def preventIdentical(self):
        return False

    def init(self):
        super(ReactiveCommunicationEventHandler, self).init()
        self.__service.onChannelMessage += self.__onChannelMessage
        self.__service.onSubscriptionClosed += self.__onSubscriptionClosed

    def fini(self):
        self.__service.onChannelMessage -= self.__onChannelMessage
        self.__service.onSubscriptionClosed -= self.__onSubscriptionClosed
        super(ReactiveCommunicationEventHandler, self).fini()

    @c2w(name='on_reactive_communication_channel_message')
    def __onChannelMessage(self, name, message):
        return {'channel_name': name, 
           'data': message}

    @c2w(name='on_reactive_communication_subscription_closed')
    def __onSubscriptionClosed(self, subscription, reason):
        return {'channel_name': (subscription.channel), 
           'subscription_id': (id(subscription)), 
           'reason': (reason.value)}
