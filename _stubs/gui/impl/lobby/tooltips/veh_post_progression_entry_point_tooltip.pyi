# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/tooltips/veh_post_progression_entry_point_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.tooltips.veh_post_progression_entry_point_tooltip_model import VehPostProgressionEntryPointTooltipModel as VehPostProgressionEntryPointTooltipModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from items import filterIntCDsByItemType as filterIntCDsByItemType, ITEM_TYPES as ITEM_TYPES
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from frameworks.wulf import PyResAccessor as PyResAccessor

class VehPostProgressionEntryPointTooltip(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    __vehicle: Any
    __parentScreen: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, intCD, parentScreen=None):
        ...
    def __getStatus(self):
        ...
