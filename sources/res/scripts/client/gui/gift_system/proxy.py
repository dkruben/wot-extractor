# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/gift_system/proxy.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/proxy.py
import logging
from gifts.gifts_common import GiftEventID
from gui.gift_system.wrappers import IncomeSysMessage
from helpers import dependency
from messenger.formatters.service_channel import ServiceChannelFormatter
from shared_utils import makeTupleByDict
from skeletons.gui.game_control import IGiftSystemController
_logger = logging.getLogger(__name__)

class GiftSystemMessagesProxy(ServiceChannelFormatter):
    __giftSystemCtrl = dependency.descriptor(IGiftSystemController)

    def format(self, message, *args):
        messageData = message.data
        if not messageData or not isinstance(messageData, dict):
            _logger.error('GiftSystemMessagesProxy received unsupported message data=%s', messageData)
            return []
        else:
            eventID = messageData.get('eventID', GiftEventID.UNKNOWN)
            eventHub = self.__giftSystemCtrl.getEventHub(eventID)
            if eventHub is not None:
                try:
                    eventHub.processMessage(makeTupleByDict(IncomeSysMessage, messageData))
                except TypeError:
                    _logger.exception('GiftSystemMessagesProxy received message with incomplete data for IncomeSysMessage')

            else:
                _logger.warning('GiftSystemMessagesProxy received message for non-existent eventID=%s', eventID)
            return []
