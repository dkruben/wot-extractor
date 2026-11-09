# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/locale/EVENT.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/locale/EVENT.py
from debug_utils import LOG_WARNING

class EVENT(object):
    PUNISHMENTWINDOW_REASON_EVENT_DESERTER = '#event:punishmentWindow/reason/event_deserter'
    PUNISHMENTWINDOW_REASON_EVENT_AFK = '#event:punishmentWindow/reason/event_afk'
    BATTLEHINTS_TESTMESSAGE = '#event:battleHints/testMessage'
    BATTLEHINTS_TESTMESSAGEWITHPARAMS = '#event:battleHints/testMessageWithParams'
    ALL_ENUM = (
     PUNISHMENTWINDOW_REASON_EVENT_DESERTER,
     PUNISHMENTWINDOW_REASON_EVENT_AFK,
     BATTLEHINTS_TESTMESSAGE,
     BATTLEHINTS_TESTMESSAGEWITHPARAMS)

    @classmethod
    def all(cls, key0):
        outcome = ('#event:{}').format(key0)
        if outcome not in cls.ALL_ENUM:
            LOG_WARNING(('Localization key "{}" not found').format(outcome))
            return None
        else:
            return outcome
