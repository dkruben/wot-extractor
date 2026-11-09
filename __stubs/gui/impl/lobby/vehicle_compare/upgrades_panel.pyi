# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/upgrades_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from helpers import dependency as dependency
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.veh_post_progression.models.progression import PostProgressionCompletion as PostProgressionCompletion
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_compare.compare_upgrades_panel_view_model import CompareUpgradesPanelViewModel as CompareUpgradesPanelViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.upgrades_model import UpgradesState as UpgradesState, UpgradesModel as UpgradesModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.vehicle_hub.sub_presenters.veh_skill_tree.utils import getFullProgressionState as getFullProgressionState
from gui.impl.pub import ViewImpl as ViewImpl
from skeletons.gui.shared import IItemsCache as IItemsCache

class CompareUpgradesPanelView(ViewImpl):
    __itemsCache: Any
    __vehItem: Any
    def __init__(self, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def update(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    # decorador original: @args2params(...)
    def __onSelectUpgrades(self, upgradeState):
        ...
    def __getSelectedState(self):
        ...
    def __hasPartialUpgrades(self):
        ...
    @staticmethod
    def __createUpgradesModel(state, isSelected):
        ...
