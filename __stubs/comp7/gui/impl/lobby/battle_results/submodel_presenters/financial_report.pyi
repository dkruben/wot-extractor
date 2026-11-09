# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/submodel_presenters/financial_report.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7.gui.impl.lobby.battle_results.comp7_financial_report_packers import Comp7CreditsStatisticsPacker as Comp7CreditsStatisticsPacker, Comp7XpDetailsPacker as Comp7XpDetailsPacker, Comp7FreeXpDetailsPacker as Comp7FreeXpDetailsPacker
from gui.battle_results.presenters.packers.economics.financial_report_packers import CrystalsDetailsPacker as CrystalsDetailsPacker, GoldStatisticsPacker as GoldStatisticsPacker
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_item_model import CurrencyRecordsItemModel as CurrencyRecordsItemModel
from gui.impl.lobby.battle_results.submodel_presenters.financial_report import FinancialReportSubPresenter as FinancialReportSubPresenter

class Comp7FinancialReportSubPresenter(FinancialReportSubPresenter):
    def packBattleResults(self, battleResults):
        ...
