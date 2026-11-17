# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/sub_presenters/battle_efficiency.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from future.utils import viewitems as viewitems
from frameworks.wulf import Array as Array
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.battle_results.pbs_helpers.common import getEnemies as getEnemies
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_item_model import DetailedPersonalEfficiencyItemModel as DetailedPersonalEfficiencyItemModel
from gui.impl.gen.view_models.views.lobby.battle_results.detailed_personal_efficiency_model import DetailedPersonalEfficiencyModel as DetailedPersonalEfficiencyModel
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.post_battle_results_view_model import PostBattleResultsViewModel as PostBattleResultsViewModel
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from gui.battle_results.reusable.shared import VehicleSummarizeInfo as VehicleSummarizeInfo
EFFICIENCY_ITEMS_TO_PROPERTIES: dict

class FrontlineBattleEfficiencySubPresenter(BattleResultsSubPresenter):
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

def getEfficiencyParametersToPropertiesMap():
    ...
