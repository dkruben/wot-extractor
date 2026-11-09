# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/indicators.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/battle/indicators.py
from __future__ import absolute_import
from gui.battle_control.battle_constants import HIT_INDICATOR_MAX_ON_SCREEN
from gui.Scaleform.daapi.view.battle.shared.indicators import _DamageIndicator
from gui.Scaleform.daapi.view.battle.shared.indicators import SixthSenseIndicator

class LSDamageIndicator(_DamageIndicator):
    _DAMAGE_INDICATOR_SWF = 'last_stand|lastStandBattleDamageIndicatorApp.swf'


def lsCreateDamageIndicator():
    return LSDamageIndicator(HIT_INDICATOR_MAX_ON_SCREEN)


class LSSixthSenseIndicator(SixthSenseIndicator):
    pass
