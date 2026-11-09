# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/tooltips/comp7_light_selector_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/tooltips/comp7_light_selector_tooltip.py
from __future__ import absolute_import
from comp7_light.gui.shared.tooltips import TOOLTIP_TYPE
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.tooltips.battle_selector import SeasonalBattleSelectorTooltip
_R_COMP7_LIGHT_SELECTOR_TOOLTIP = R.strings.comp7_light.selectorTooltip
_TOOLTIP_MIN_WIDTH = 280

class Comp7LightSelectorTooltip(SeasonalBattleSelectorTooltip):
    _TOOLTIP_TYPE = TOOLTIP_TYPE.COMP7_LIGHT_SELECTOR_INFO
    _TOOLTIP_WIDTH = _TOOLTIP_MIN_WIDTH

    @staticmethod
    def _getTitle():
        return backport.text(_R_COMP7_LIGHT_SELECTOR_TOOLTIP.title())

    @staticmethod
    def _getDescription():
        return backport.text(_R_COMP7_LIGHT_SELECTOR_TOOLTIP.desc())
