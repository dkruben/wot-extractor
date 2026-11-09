# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/indicators.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/indicators.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.battle.shared.indicators import SixthSenseIndicator
from gui.Scaleform.daapi.view.battle.shared.indicators import _DamageIndicator
from gui.battle_control.battle_constants import HIT_INDICATOR_MAX_ON_SCREEN

class HWDamageIndicator(_DamageIndicator):
    _DAMAGE_INDICATOR_SWF = 'halloween|halloweenBattleDamageIndicatorApp.swf'


def hwCreateDamageIndicator():
    return HWDamageIndicator(HIT_INDICATOR_MAX_ON_SCREEN)


class HalloweenSixthSenseIndicator(SixthSenseIndicator):
    pass
