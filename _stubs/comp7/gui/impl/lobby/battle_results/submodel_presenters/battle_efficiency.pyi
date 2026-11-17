# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/submodel_presenters/battle_efficiency.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.comp7_battle_results_view_model import Comp7BattleResultsViewModel as Comp7BattleResultsViewModel
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_item_model import DetailedPersonalEfficiencyItemModel as DetailedPersonalEfficiencyItemModel
from gui.impl.lobby.battle_results.submodel_presenters.battle_efficiency import getEfficiencyParametersToPropertiesMap as getEfficiencyParametersToPropertiesMap
from gui.impl.lobby.tooltips.battle_efficiency_tooltips_views import BattleResultsCriticalDamageTooltipView as BattleResultsCriticalDamageTooltipView, BattleResultsStatsTooltipView as BattleResultsStatsTooltipView
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.battle_results.pbs_helpers.common import getEnemies as getEnemies
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_model import DetailedPersonalEfficiencyModel as DetailedPersonalEfficiencyModel
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from comp7_core.gui.battle_results.reusable.shared import Comp7CoreVehicleSummarizeInfo as Comp7CoreVehicleSummarizeInfo

class Comp7BattleEfficiencySubPresenter(BattleResultsSubPresenter):
    __comp7Controller: Any
    __itemsCache: Any
    @classmethod
    def getViewModelType(cls):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def packBattleResults(self, battleResults):
        ...
    def __packDetailedPersonalEfficiency(self, model, battleResults):
        ...
    def __packDetailedPersonalInfo(self, model, player):
        ...
    def __packVehicleSummarizeEfficiency(self, model, battleResults):
        ...
