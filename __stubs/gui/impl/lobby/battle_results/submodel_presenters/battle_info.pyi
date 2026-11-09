# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/submodel_presenters/battle_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_results.pbs_helpers.common import getArenaNameStr as getArenaNameStr, getRegularFinishResultResource as getRegularFinishResultResource
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD, PLAYER_TEAM_RESULT as PLAYER_TEAM_RESULT
from gui.impl.gen.view_models.views.lobby.battle_results.random.random_battle_info_model import RandomBattleInfoModel as RandomBattleInfoModel
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class BattleInfoSubPresenter(BattleResultsSubPresenter):
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
