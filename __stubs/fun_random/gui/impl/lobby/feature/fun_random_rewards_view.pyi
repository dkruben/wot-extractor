# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/feature/fun_random_rewards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from frameworks.wulf import ViewSettings as ViewSettings
from frameworks.wulf import WindowLayer as WindowLayer
from fun_random.gui.feature.fun_sounds import FUN_REWARD_SCREEN_SOUND_SPACE as FUN_REWARD_SCREEN_SOUND_SPACE
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin
from fun_random.gui.impl.gen.view_models.views.lobby.feature.fun_random_rewards_view_model import FunRandomRewardsViewModel as FunRandomRewardsViewModel
from fun_random.gui.impl.lobby.common.fun_view_helpers import getCompensatedFunRandomBonusPacker as getCompensatedFunRandomBonusPacker
from gui.impl.auxiliary.tooltips.compensation_tooltip import VehicleCompensationTooltipContent as VehicleCompensationTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_types import LootBoxCompensationTooltipTypes as LootBoxCompensationTooltipTypes
from gui.impl.gen.view_models.views.loot_box_vehicle_compensation_tooltip_model import LootBoxVehicleCompensationTooltipModel as LootBoxVehicleCompensationTooltipModel
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses, LootBoxTokensBonus as LootBoxTokensBonus

class FunRandomLootBoxAwardView(ViewImpl, FunAssetPacksMixin):
    __slots__: tuple
    _COMMON_SOUND_SPACE = FUN_REWARD_SCREEN_SOUND_SPACE
    __tooltips: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, data, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __onCloseClick(self):
        ...
    def __packRewards(self, rewardsModel, rewards, packer):
        ...

class FunRandomLootBoxAwardWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, data=None):
        ...
