# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/submodel_presenters/financial_report.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/lobby/battle_results/submodel_presenters/financial_report.py
from __future__ import absolute_import
from comp7.gui.impl.lobby.battle_results.comp7_financial_report_packers import Comp7CreditsStatisticsPacker, Comp7XpDetailsPacker, Comp7FreeXpDetailsPacker
from gui.battle_results.presenters.packers.economics.financial_report_packers import CrystalsDetailsPacker, GoldStatisticsPacker
from gui.impl.gen.view_models.views.lobby.battle_results.currency_records_item_model import CurrencyRecordsItemModel
from gui.impl.lobby.battle_results.submodel_presenters.financial_report import FinancialReportSubPresenter

class Comp7FinancialReportSubPresenter(FinancialReportSubPresenter):

    def packBattleResults(self, battleResults):
        viewModel = self.getViewModel()
        CrystalsDetailsPacker.packModel(viewModel.crystals, CurrencyRecordsItemModel.CRYSTAL, battleResults)
        Comp7XpDetailsPacker.packModel(viewModel.xp, CurrencyRecordsItemModel.XP_COST, battleResults)
        Comp7FreeXpDetailsPacker.packModel(viewModel.freeXp, CurrencyRecordsItemModel.FREE_XP, battleResults)
        Comp7CreditsStatisticsPacker.packModel(viewModel.credits, CurrencyRecordsItemModel.CREDITS, battleResults)
        GoldStatisticsPacker.packModel(viewModel.gold, CurrencyRecordsItemModel.GOLD, battleResults)
