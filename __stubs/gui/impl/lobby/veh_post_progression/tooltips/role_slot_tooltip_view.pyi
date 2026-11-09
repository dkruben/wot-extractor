# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_post_progression/tooltips/role_slot_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.daapi.view.lobby.veh_post_progression.veh_post_progression_vehicle import g_postProgressionVehicle as g_postProgressionVehicle
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.role_model import RoleModel as RoleModel
from gui.impl.gen.view_models.views.lobby.post_progression.tooltip.role_slot_tooltip_view_model import RoleSlotTooltipViewModel as RoleSlotTooltipViewModel
from gui.impl.lobby.veh_post_progression.tooltips.base_feature_tooltip_view import BaseFeatureTooltipView as BaseFeatureTooltipView
from gui.impl.wrappers.user_compound_price_model import PriceModelBuilder as PriceModelBuilder, BuyPriceModelBuilder as BuyPriceModelBuilder
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.shared import IItemsCache as IItemsCache
from items.components.supply_slots_components import SupplySlot as SupplySlot

class RoleSlotTooltipView(BaseFeatureTooltipView):
    _itemsCache: Any
    __slots__: tuple
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, step, *args, **kwargs):
        ...
    def __fillRolesData(self, model):
        ...
    def __fillRole(self, roleModel, slot):
        ...
