# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/mapbox/mapbox_bonus_packers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/mapbox/mapbox_bonus_packers.py
import typing
from gui.impl.auxiliary.rewards_helper import BlueprintBonusTypes
from gui.shared.missions.packers.bonus import BonusUIPacker, BlueprintBonusUIPacker, getDefaultBonusPackersMap
from shared_utils import first
if typing.TYPE_CHECKING:
    from frameworks.wulf import Array

def getMapboxBonusPacker():
    mapping = getDefaultBonusPackersMap()
    mapping.update({(BlueprintBonusTypes.BLUEPRINTS): _MapboxBlueprintBonusUIPacker, 
       (BlueprintBonusTypes.FINAL_BLUEPRINTS): _MapboxBlueprintBonusUIPacker, 
       (BlueprintBonusTypes.BLUEPRINTS_ANY): _MapboxBlueprintBonusUIPacker})
    return BonusUIPacker(mapping)


def packMapboxRewardModelAndTooltip(rewardsList, bonusList, packer, numBattles, tooltipsList=None):
    groupStartIdx = len(tooltipsList)
    groupIdx = 0
    for bonusItem in bonusList:
        totalIdx = groupStartIdx + groupIdx
        tooltipsData = packer.getToolTip(bonusItem)
        for bonusIdx, bonusModel in enumerate(packer.pack(bonusItem)):
            bonusModel.setTooltipId(str(totalIdx + bonusIdx))
            bonusModel.setIndex(groupIdx)
            if tooltipsList is not None:
                tooltipsList.append(tooltipsData[bonusIdx])
            groupIdx += 1
            rewardsList.addViewModel(bonusModel)

    return


class _MapboxBlueprintBonusUIPacker(BlueprintBonusUIPacker):

    @classmethod
    def _pack(cls, bonus):
        models = super(_MapboxBlueprintBonusUIPacker, cls)._pack(bonus)
        model = first(models)
        if model:
            model.setLabel(bonus.getLabel())
        return models
