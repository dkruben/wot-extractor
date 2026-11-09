# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/battle_hints/common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/battle_hints/common.py
from __future__ import absolute_import
import logging
from hints_common.battle.schemas.const import MAX_PRIORITY
DEFAULT_LOGGER_NAME = 'BattleHints'
HIGHEST_PRIORITY = MAX_PRIORITY + 1
HIDE_ANIMATION_TIMEOUT = 2.0
QUEUE_HINTS_MAX_SIZE = 200

def getLogger(*names):
    return logging.getLogger(('{}').format((':').join((DEFAULT_LOGGER_NAME,) + names)))
