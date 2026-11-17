# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/veh_skill_tree/tooltips/base_perk_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array
from gui.veh_post_progression.models.modifications import SimpleModItem as SimpleModItem
from helpers import dependency as dependency
from gui.impl.gen.view_models.views.lobby.veh_skill_tree.tooltips.base_perk_tooltip_model import BasePerkTooltipModel as BasePerkTooltipModel
from gui.impl.gen.view_models.views.lobby.veh_skill_tree.tooltips.kpi_model import KpiModel as KpiModel
from gui.impl.gen.view_models.views.lobby.veh_skill_tree.tooltips.kpi_value_model import KpiValueModel as KpiValueModel
from gui.impl.lobby.vehicle_hub.sub_presenters.veh_skill_tree.utils import fillNodeModel as fillNodeModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items import Vehicle as Vehicle
from skeletons.gui.shared import IItemsCache as IItemsCache

class BasePerkTooltipView(ViewImpl):
    __itemsCache: Any
    @property
    def viewModel(self):
        ...
    def _onLoading(self, vehCD, step, stepStatus, *args, **kwargs):
        ...
    @staticmethod
    def __fillModifiers(vehicle, modifiers, modification):
        ...
