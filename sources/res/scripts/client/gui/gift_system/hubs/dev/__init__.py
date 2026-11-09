# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/gift_system/hubs/dev/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/gift_system/hubs/dev/__init__.py
from gui import SystemMessages
from gui.shared.formatters import text_styles

class IDevMessagesPusher(object):

    @classmethod
    def _formatMessage(cls, message):
        return text_styles.stats(message)

    @classmethod
    def _pushClientMessage(cls, message):
        SystemMessages.pushMessage(cls._formatMessage(message), SystemMessages.SM_TYPE.MediumInfo)
