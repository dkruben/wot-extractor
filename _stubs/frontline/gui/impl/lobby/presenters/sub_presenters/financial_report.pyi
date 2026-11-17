# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/sub_presenters/financial_report.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.vehicle_financial_report_model import VehicleFinancialReportModel as VehicleFinancialReportModel
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_item_model import CurrencyRecordsItemModel as CurrencyRecordsItemModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.shared import events as events
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.battle_financial_report_model import BattleFinancialReportModel as BattleFinancialReportModel
from frontline.gui.financial_report_packers import FrontlineCrystalsDetailsPacker as FrontlineCrystalsDetailsPacker, FrontlineXpDetailsPacker as FrontlineXpDetailsPacker, FrontlineFreeXpDetailsPacker as FrontlineFreeXpDetailsPacker, FrontlineCreditsStatisticsPacker as FrontlineCreditsStatisticsPacker, FrontlineGoldStatisticsPacker as FrontlineGoldStatisticsPacker
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS as VEHICLE_TAGS
from frameworks.wulf import ViewModel as ViewModel

class FrontlineFinancialReportSubPresenter(BattleResultsSubPresenter):
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
    def getVehBattleResultsModel(self, vehicle, battleResults, vehIdx):
        ...
    def _getListeners(self):
        ...
    def _getCallbacks(self):
        ...
    def __onXpBonusStatusChanged(self, _=None):
        ...
