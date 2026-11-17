# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/sub_presenters/battle_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from fort_rush.gui.battle_results.pbs_helpers import makeFortRushFinishResultLabel as makeFortRushFinishResultLabel
from fort_rush.gui.impl.gen.view_models.views.lobby.post_battle_results_view.battle_info_model import BattleInfoModel as BattleInfoModel
from gui.battle_results.pbs_helpers.common import getArenaNameStr as getArenaNameStr
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class FortRushBattleInfoSubPresenter(BattleResultsSubPresenter):
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
