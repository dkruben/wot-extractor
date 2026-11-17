# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/sub_presenters/battle_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_results.pbs_helpers.common import getArenaNameStr as getArenaNameStr
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD
from frontline.gui.impl.gen.view_models.views.lobby.views.post_battle_results_view.battle_info_model import BattleInfoModel as BattleInfoModel
from frontline.gui.frontline_helpers import FLBattleTypeDescription as FLBattleTypeDescription
from frontline.gui.frontline_helpers import makeNewEpicBattleFinishResultLabel as makeNewEpicBattleFinishResultLabel
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class FrontlineBattleInfoSubPresenter(BattleResultsSubPresenter):
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...
