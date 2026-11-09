# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_post_progression/tooltips/pair_modification_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.common.bonus_value_model import BonusValueModel as BonusValueModel
from gui.impl.gen.view_models.views.lobby.post_progression.modification_model import ModificationModel as ModificationModel
from gui.impl.gen.view_models.views.lobby.post_progression.step_model import StepState as StepState
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.pair_modification_tooltip_view_model import PairModificationTooltipViewModel as PairModificationTooltipViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.wrappers.user_compound_price_model import PriceModelBuilder as PriceModelBuilder, BuyPriceModelBuilder as BuyPriceModelBuilder
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf import Array as Array
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.veh_post_progression.models.modifications import MultiModsItem as MultiModsItem, SimpleModItem as SimpleModItem
from gui.veh_post_progression.models.progression_step import PostProgressionStepItem as PostProgressionStepItem

class BasePairModificationTooltipView(ViewImpl):
    __slots__: tuple
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, vehicle, stepID, modificationId, *args, **kwargs):
        ...
    def _getState(self, step, modificationId):
        ...
    def __fillModifications(self, modifications, pairModification):
        ...
    def __fillModifiers(self, vehicle, modifiers, modification):
        ...

class CmpPairModificationTooltipView(BasePairModificationTooltipView):
    __slots__: tuple
    def _onLoading(self, vehicle, stepID, modificationId, *args, **kwargs):
        ...
    def _getState(self, step, modificationId):
        ...

class CmpPanelPairModificationTooltipView(CmpPairModificationTooltipView):
    __slots__: tuple
    def _onLoading(self, vehicle, stepID, modificationId, *args, **kwargs):
        ...

class CfgPairModificationTooltipView(BasePairModificationTooltipView):
    _itemsCache: Any
    __slots__: tuple
    @property
    def viewModel(self):
        ...
    def _onLoading(self, vehicle, stepID, modificationId, *args, **kwargs):
        ...
