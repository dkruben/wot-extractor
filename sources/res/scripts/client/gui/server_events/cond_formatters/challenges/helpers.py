# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/server_events/cond_formatters/challenges/helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/server_events/cond_formatters/challenges/helpers.py
from __future__ import absolute_import
import logging
from gui.impl import backport
from gui.server_events.cond_formatters import FORMATTER_IDS, FormattableField
from gui.server_events.cond_formatters.challenges.constants import DEFAULT_CONDITION_TITLE_TEXT_RES, DEFAULT_CONDITION_TEXT_RES
_logger = logging.getLogger(__name__)

def _createText(textRes, defaultRes, **kwargs):
    if not textRes.exists():
        return backport.text(defaultRes())
    return backport.text(textRes(), **kwargs)


def packDescriptionField(textRes, **kwargs):
    return FormattableField(FORMATTER_IDS.DESCRIPTION, (
     _createText(textRes, DEFAULT_CONDITION_TEXT_RES, **kwargs),))


def packTitleField(textRes, **kwargs):
    return FormattableField(FORMATTER_IDS.SIMPLE_TITLE, (
     _createText(textRes, DEFAULT_CONDITION_TITLE_TEXT_RES, **kwargs),))


def getRelationValue(condition):
    if condition.relationValue is not None:
        return backport.getNiceNumberFormat(condition.relationValue)
    else:
        _logger.error('Undefined relation value for condition: %s', condition.getData())
        return -1
