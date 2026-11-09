# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarFairplayMessageComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarFairplayMessageComponent.py
from __future__ import absolute_import
import logging
from BigWorld import DynamicScriptComponent
import SoundGroups
from gui.shared.utils import showAFKWarningInWindowsBar
from messenger.proto.events import g_messengerEvents
from messenger.proto.shared_messages import ClientActionTemplateMessage, ACTION_MESSAGE_TYPE
_logger = logging.getLogger(__name__)
AFK_WARNING_MESSAGE_SOUND = 'afk_warning_message'

class AvatarFairplayMessageComponent(DynamicScriptComponent):

    def showWarningMessage(self, templateKey):
        _logger.debug('AvatarFairplayMessageComponent.showMessage: %s', templateKey)
        message = ClientActionTemplateMessage(templateKey, ACTION_MESSAGE_TYPE.FAIRPLAY_WARNING)
        g_messengerEvents.onCustomMessage(message)
        showAFKWarningInWindowsBar()
        SoundGroups.g_instance.playSound2D(AFK_WARNING_MESSAGE_SOUND)
