# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/submodels/common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl.gen.view_models.views.lobby.lootbox_system.box_info_model import BoxInfoModel as BoxInfoModel
from gui.lootbox_system.base.utils import getIsAnimationActive as getIsAnimationActive, setIsAnimationActive as setIsAnimationActive
from helpers import dependency as dependency
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from typing import Dict as Dict, Union as Union
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.home_view_model import HomeViewModel as HomeViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.single_box_rewards_view_model import SingleBoxRewardsViewModel as SingleBoxRewardsViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.multiple_boxes_rewards_view_model import MultipleBoxesRewardsViewModel as MultipleBoxesRewardsViewModel
from gui.shared.gui_items.loot_box import LootBox as LootBox
IAnimatedViewModel: Any

# decorador original: @dependency.replace_none_kwargs(...)
def updateBoxesInfoModel(eventName, boxesInfo, lootBoxes=None):
    ...
def updateAnimationState(model, ctx, eventName):
    ...
