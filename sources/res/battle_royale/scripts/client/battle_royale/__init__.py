# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/__init__.py
from __future__ import absolute_import
from chat_shared import SYS_MESSAGE_TYPE
from battle_royale_progression_common.battle_royale_progression_constants import SM_TYPES

def registerSystemMessagesTypes():
    SYS_MESSAGE_TYPE.inject(SM_TYPES)


def initProgression():
    registerSystemMessagesTypes()
    from battle_royale.gui.game_control import registerBRProgressionAwardControllers
    registerBRProgressionAwardControllers()
    from battle_royale.notification import registerClientNotificationHandlers
    registerClientNotificationHandlers()
    from battle_royale.messenger.formatters import registerMessengerServerFormatters
    registerMessengerServerFormatters()
