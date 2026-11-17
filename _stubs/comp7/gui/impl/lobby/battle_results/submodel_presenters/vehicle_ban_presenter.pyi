# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/submodel_presenters/vehicle_ban_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_bans_model import Comp7BansModel as Comp7BansModel
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
from frameworks.wulf import ViewModel as ViewModel

class Comp7VehicleBanSubPresenter(BattleResultsSubPresenter):
    __itemsCache: Any
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
