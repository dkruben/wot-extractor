# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/demount_kit_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/demount_kit_builders.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts, advanced, demount_kits
from gui.shared.tooltips.builders import AdvancedDataBuilder, DefaultFormatBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     AdvancedDataBuilder(TOOLTIPS_CONSTANTS.AWARD_DEMOUNT_KIT, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, demount_kits.DemountKitToolTipData(contexts.DemountKitContext()), advanced.DemountKitTooltipAdvanced(contexts.DemountKitContext())),
     DefaultFormatBuilder(TOOLTIPS_CONSTANTS.NOT_ENOUGH_MONEY, TOOLTIPS_CONSTANTS.COMPLEX_UI, demount_kits.NotEnoughMoneyTooltipData(contexts.ToolTipContext(None))),
     AlternativeGoldTooltipBuilder(TOOLTIPS_CONSTANTS.GOLD_ALTERNATIVE_STATS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, demount_kits.GoldStatsToolTipData(contexts.ToolTipContext(None)), advanced.MoneyAndXpAdvanced(contexts.ToolTipContext(None))),
     AlternativeGoldTooltipBuilder(TOOLTIPS_CONSTANTS.GOLD_ALTERNATIVE_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, demount_kits.GoldToolTipData(contexts.ToolTipContext(None)), advanced.MoneyAndXpAdvanced(contexts.ToolTipContext(None))))


class AlternativeGoldTooltipBuilder(AdvancedDataBuilder):
    __slots__ = ('__btnType', )

    def __init__(self, tooltipType, linkage, provider, adProvider):
        super(AlternativeGoldTooltipBuilder, self).__init__(tooltipType, linkage, provider, adProvider)
        self.__btnType = CURRENCIES_CONSTANTS.GOLD

    def _buildData(self, _advanced, *args, **kwargs):
        return super(AlternativeGoldTooltipBuilder, self)._buildData(_advanced, self.__btnType)
