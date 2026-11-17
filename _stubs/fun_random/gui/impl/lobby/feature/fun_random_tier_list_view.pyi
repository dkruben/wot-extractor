# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/feature/fun_random_tier_list_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from constants import Configs as Configs
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from fun_random.gui.feature.fun_sounds import FUN_TIER_LIST_SOUND_SPACE as FUN_TIER_LIST_SOUND_SPACE
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher as FunProgressionWatcher, FunAssetPacksMixin as FunAssetPacksMixin
from fun_random.gui.feature.util.fun_wrappers import hasActiveProgression as hasActiveProgression
from fun_random.gui.impl.gen.view_models.views.lobby.feature.fun_random_tier_list_view_model import FunRandomTierListViewModel as FunRandomTierListViewModel
from fun_random.gui.impl.lobby.common.fun_view_helpers import RARITY_ORDER as RARITY_ORDER, getFunRandomBonusPacker as getFunRandomBonusPacker
from fun_random.gui.impl.lobby.common.lootboxes import FEP_CATEGORY as FEP_CATEGORY, packLootboxes as packLootboxes
from gui.impl.auxiliary.tooltips.compensation_tooltip import VehicleCompensationTooltipContent as VehicleCompensationTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_types import LootBoxCompensationTooltipTypes as LootBoxCompensationTooltipTypes
from gui.impl.gen.view_models.views.loot_box_vehicle_compensation_tooltip_model import LootBoxVehicleCompensationTooltipModel as LootBoxVehicleCompensationTooltipModel
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency, server_settings as server_settings
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class FunRandomTierListView(ViewImpl, FunProgressionWatcher, FunAssetPacksMixin):
    __lobbyContext: Any
    __itemsCache: Any
    __slots__: tuple
    _COMMON_SOUND_SPACE = FUN_TIER_LIST_SOUND_SPACE
    __tooltips: Any
    def __init__(self, layoutID):
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
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, _):
        ...
    # decorador original: @hasActiveProgression(...)
    def __update(self):
        ...
