# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/submodels/common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/lootbox_system/base/submodels/common.py
from typing import TYPE_CHECKING
from gui.impl.gen.view_models.views.lobby.lootbox_system.box_info_model import BoxInfoModel
from gui.lootbox_system.base.utils import getIsAnimationActive, setIsAnimationActive
from helpers import dependency
from skeletons.gui.game_control import ILootBoxSystemController
if TYPE_CHECKING:
    from typing import Dict, Union
    from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.home_view_model import HomeViewModel
    from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.single_box_rewards_view_model import SingleBoxRewardsViewModel
    from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.multiple_boxes_rewards_view_model import MultipleBoxesRewardsViewModel
    from gui.shared.gui_items.loot_box import LootBox
    IAnimatedViewModel = Union[(HomeViewModel, SingleBoxRewardsViewModel, MultipleBoxesRewardsViewModel)]

@dependency.replace_none_kwargs(lootBoxes=ILootBoxSystemController)
def updateBoxesInfoModel(eventName, boxesInfo, lootBoxes=None):
    boxesInfo.clear()
    for box in lootBoxes.getActiveBoxes(eventName):
        boxInfo = BoxInfoModel()
        boxInfo.setBoxCategory(box.getCategory())
        boxInfo.setBoxesCount(box.getInventoryCount())
        boxInfo.setBoxesCountToGuaranteed(lootBoxes.getBoxInfo(box.getID())['boxCountToGuaranteedBonus'])
        boxesInfo.addViewModel(boxInfo)

    boxesInfo.invalidate()


def updateAnimationState(model, ctx, eventName):
    isAnimationActive = (ctx or {}).get('isAnimationActive')
    if isAnimationActive is None:
        isAnimationActive = getIsAnimationActive(eventName)
    else:
        setIsAnimationActive(eventName, isAnimationActive)
    model.setIsAnimationActive(isAnimationActive)
    return
