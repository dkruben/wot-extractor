# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/tooltips/battle_pass_builders.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/tooltips/battle_pass_builders.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import contexts, battle_pass
from gui.shared.tooltips.builders import DataBuilder
__all__ = ('getTooltipBuilders', )

def getTooltipBuilders():
    return (
     DataBuilder(TOOLTIPS_CONSTANTS.BATTLE_PASS_GIFT_TOKEN, TOOLTIPS_CONSTANTS.BATTLE_PASS_GIFT_TOKEN_UI, battle_pass.BattlePassGiftTokenTooltipData(contexts.BattlePassGiftTokenContext())),
     DataBuilder(TOOLTIPS_CONSTANTS.BATTLE_PASS_POINTS, TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI, battle_pass.BattlePassPointsTooltipData(contexts.ToolTipContext(None))))
