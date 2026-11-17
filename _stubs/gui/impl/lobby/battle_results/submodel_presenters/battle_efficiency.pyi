# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/submodel_presenters/battle_efficiency.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf import Array as Array
from gui.impl.lobby.tooltips.battle_efficiency_tooltips_views import BattleResultsStatsTooltipView as BattleResultsStatsTooltipView, BattleResultsCriticalDamageTooltipView as BattleResultsCriticalDamageTooltipView
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.battle_results.pbs_helpers.common import getEnemies as getEnemies
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_item_model import DetailedPersonalEfficiencyItemModel as DetailedPersonalEfficiencyItemModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_model import DetailedPersonalEfficiencyModel as DetailedPersonalEfficiencyModel
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_battle_results_view_model import RandomBattleResultsViewModel as RandomBattleResultsViewModel
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo
from gui.impl.gen.view_models.views.lobby.battle_results.base_capture_info_model import BaseCaptureInfoModel as BaseCaptureInfoModel
EFFICIENCY_ITEMS_TO_PROPERTIES: dict

class BattleEfficiencySubPresenter(BattleResultsSubPresenter):
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
    def __packBaseCaptureInfo(self, model, battleResults):
        ...

def getEfficiencyParametersToPropertiesMap():
    ...
