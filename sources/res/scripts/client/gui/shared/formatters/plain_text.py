# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/formatters/plain_text.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/formatters/plain_text.py
from __future__ import absolute_import
from gui.server_events.cond_formatters import FORMATTER_IDS
from gui.server_events import formatters
from gui.shared.formatters import text_styles

def getDefaultPlainTextFormatters():
    return {(FORMATTER_IDS.SIMPLE_TITLE): (formatters.titleFormatPlain), 
       (FORMATTER_IDS.CUMULATIVE): (formatters.titleCumulativeFormatPlain), 
       (FORMATTER_IDS.COMPLEX): (formatters.titleComplexFormatPlain), 
       (FORMATTER_IDS.RELATION): (formatters.titleRelationFormatPlain), 
       (FORMATTER_IDS.DESCRIPTION): (text_styles.highlightTextPlain), 
       (FORMATTER_IDS.COMPLEX_RELATION): (formatters.titleComplexRelationFormatPlain)}


class PlainTextFormatter(object):
    _formatters = getDefaultPlainTextFormatters()

    @classmethod
    def getPlainTextFromFormattedField(cls, formattableField):
        formatterName = formattableField.formatterID
        formatter = cls._formatters.get(formatterName)
        text = formatter(*formattableField.args)
        return text
