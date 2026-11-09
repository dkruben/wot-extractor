# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/helpers/tips.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/helpers/tips.py
from __future__ import absolute_import
import typing
from comp7_light_constants import ARENA_GUI_TYPE
from helpers.tips import readTips
from comp7_core.helpers.tips import Comp7BaseTipsCriteria
_COMP7_LIGHT_TIPS_PATTERN = '^(comp7(Core|Light)\\d+$)'
_comp7LightTips = readTips(_COMP7_LIGHT_TIPS_PATTERN)

class Comp7LightTipsCriteria(Comp7BaseTipsCriteria):

    def _getArenaGuiType(self):
        return ARENA_GUI_TYPE.COMP7_LIGHT

    @staticmethod
    def _getRegularTips():
        return _comp7LightTips
