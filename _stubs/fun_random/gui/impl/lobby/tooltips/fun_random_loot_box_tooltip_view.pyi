# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_loot_box_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin as FunAssetPacksMixin
from fun_random.gui.impl.gen.view_models.views.lobby.tooltips.fun_random_loot_box_tooltip_view_model import FunRandomLootBoxTooltipViewModel as FunRandomLootBoxTooltipViewModel
from fun_random.gui.impl.lobby.common.fun_view_helpers import getFunRandomBonusPacker as getFunRandomBonusPacker
from fun_random.gui.impl.lobby.common.lootboxes import packLootboxRewards as packLootboxRewards
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class FunRandomLootBoxTooltipView(ViewImpl, FunAssetPacksMixin):
    __slots__: tuple
    __itemsCache: Any
    __lobbyContext: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, lootboxTokenID, *args, **kwargs):
        ...
