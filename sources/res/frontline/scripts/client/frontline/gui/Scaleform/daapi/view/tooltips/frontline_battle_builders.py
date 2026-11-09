# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/tooltips/frontline_battle_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/tooltips/frontline_battle_builders.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips.builders import DataBuilder
from frontline.gui.shared.tooltips.FLRandomReserve import FLRandomReserve
from frontline.gui.Scaleform.daapi.view.battle.tooltips.epic_battle_tooltips import EpicRankUnlockTooltipData, _FLRandomReserveContext
from gui.shared.tooltips import contexts
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.FRONTLINE_RANDOM_RESERVE, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, FLRandomReserve(_FLRandomReserveContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.EPIC_RANK_UNLOCK_INFO, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, EpicRankUnlockTooltipData(contexts.ToolTipContext(None))))
