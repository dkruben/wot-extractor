# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/common/view_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/common/view_helpers.py
from __future__ import absolute_import
import logging, typing
from gui.server_events.bonuses import processAttachmentsSetTokens
from gui.shared.missions.packers.bonus import getDefaultBonusPacker
if typing.TYPE_CHECKING:
    from typing import TypeVar, Optional, Dict, List
    from frameworks.wulf import Array
    from gui.server_events.bonuses import SimpleBonus
    from gui.shared.missions.packers.bonus import BonusUIPacker
    from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
    BonusModelType = TypeVar('BonusModelType', bound=BonusModel)
_logger = logging.getLogger(__name__)

def packBonusModelAndTooltipData(bonuses, bonusModelsList, tooltipData=None, packer=None, showAttachmentsSets=False):
    packer = packer or getDefaultBonusPacker()
    tooltipIndex = 0 if tooltipData is None else len(tooltipData)
    bonuses = processAttachmentsSetTokens(bonuses, showAttachmentsSets=showAttachmentsSets)
    for bonus in (b for b in bonuses if b.isShowInGUI()):
        bonusList = packer.pack(bonus)
        withTooltips = bonusList and tooltipData is not None
        bTooltipList = packer.getToolTip(bonus) if withTooltips else []
        bContentIdList = packer.getContentId(bonus) if withTooltips else []
        if len(bonusList) != len(bTooltipList) and withTooltips:
            _logger.warning('bonusList and bTooltipList mismatch! Bonus: %s', bonus)
        if len(bonusList) != len(bContentIdList) and withTooltips:
            _logger.warning('bonusList and bContentIdList mismatch! Bonus: %s', bonus)
        for bIndex, bModel in enumerate(bonusList):
            bModel.setIndex(bIndex)
            tooltipIndex = _packBonusTooltip(bModel, bIndex, bTooltipList, bContentIdList, tooltipData, tooltipIndex)
            bonusModelsList.addViewModel(bModel)

        bonusModelsList.invalidate()

    return


def _packBonusTooltip(bonusModel, bonusIndex, bonusTooltipList, bonusContentIdList, tooltipData, tooltipIndex):
    if tooltipData is None or not bonusTooltipList and not bonusContentIdList:
        return tooltipIndex
    tooltipIdx = str(tooltipIndex)
    bonusModel.setTooltipId(tooltipIdx)
    if bonusTooltipList:
        tooltipData[tooltipIdx] = bonusTooltipList[bonusIndex]
    if bonusContentIdList:
        bonusModel.setTooltipContentId(str(bonusContentIdList[bonusIndex]))
    return tooltipIndex + 1
