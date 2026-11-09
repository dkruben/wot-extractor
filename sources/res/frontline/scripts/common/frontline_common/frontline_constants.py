# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/common/frontline_common/frontline_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/common/frontline_common/frontline_constants.py
from __future__ import absolute_import
from future.utils import viewitems
EMPTY_SETUP_RESERVES_MODIFIER = -1

class FLBattleReservesModifier(object):
    STANDARD = 0
    FAST = 1
    RANDOM = 2


RESERVES_MODIFIER_NAMES = {v: k.lower() for k, v in viewitems(FLBattleReservesModifier.__dict__) if not k.startswith('__')}
RESERVES_MODIFIER_IDS = {v: k for k, v in viewitems(RESERVES_MODIFIER_NAMES)}
