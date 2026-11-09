# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/gf_notifications/utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/gf_notifications/utils.py
import typing, uuid
from gui.impl.lobby.gf_notifications.cache import getCache
from messenger.m_constants import SCH_CLIENT_MSG_TYPE
from helpers import dependency
from skeletons.gui.system_messages import ISystemMessages
if typing.TYPE_CHECKING:
    from gui.impl.lobby.gf_notifications.constants import GFNotificationTemplates

@dependency.replace_none_kwargs(systemMessages=ISystemMessages)
def pushGFNotification(gfTemplate, data, notificationGuiSettings=None, systemMessages=None):
    gfDataID = str(uuid.uuid4())
    getCache().setPayload(gfDataID, data)
    systemMessages.proto.serviceChannel.pushClientMessage({'data': {'gfDataID': gfDataID}, 
       'template': gfTemplate, 
       'notificationGuiSettings': (notificationGuiSettings if notificationGuiSettings else dict())}, msgType=SCH_CLIENT_MSG_TYPE.GF_SM_TYPE)
