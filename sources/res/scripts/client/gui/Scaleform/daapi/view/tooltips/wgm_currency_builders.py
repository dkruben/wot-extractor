# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/wgm_currency_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/wgm_currency_builders.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts
from gui.shared.tooltips import wgm_currency
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

class CurrencyTooltipBuilder(DataBuilder):
    __slots__ = ('__btnType', '__hideActionBlock')

    def __init__(self, btnType, tooltipType, linkage, hideActionBlock=False):
        super(CurrencyTooltipBuilder, self).__init__(tooltipType, linkage, wgm_currency.WGMCurrencyTooltip(contexts.ToolTipContext(None)))
        self.__btnType = btnType
        self.__hideActionBlock = hideActionBlock
        return

    def _buildData(self, advanced, *args):
        return super(CurrencyTooltipBuilder, self)._buildData(advanced, self.__btnType, self.__hideActionBlock)


def getTooltipBuilders():
    return (
     CurrencyTooltipBuilder(CURRENCIES_CONSTANTS.GOLD, TOOLTIPS_CONSTANTS.GOLD_STATS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI),
     CurrencyTooltipBuilder(CURRENCIES_CONSTANTS.CREDITS, TOOLTIPS_CONSTANTS.CREDITS_STATS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI),
     CurrencyTooltipBuilder(CURRENCIES_CONSTANTS.CREDITS, TOOLTIPS_CONSTANTS.CREDITS_STATS_FULL_SCREEN, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, True),
     CurrencyTooltipBuilder(CURRENCIES_CONSTANTS.GOLD, TOOLTIPS_CONSTANTS.GOLD_STATS_FULL_SCREEN, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, True))
