# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/submodel_presenters/battle_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from comp7.gui.impl.gen.view_models.views.lobby.battle_results.comp7_battle_info_model import Comp7BattleInfoModel as Comp7BattleInfoModel
from comp7_core_constants import FINISH_REASON as FINISH_REASON
from fairplay_violation_types import FairplayViolations as FairplayViolations
from gui.impl.gen import R as R
from gui.impl.lobby.battle_results.submodel_presenters.battle_info import BattleInfoSubPresenter as BattleInfoSubPresenter
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.stats_ctrl import BattleResults as BattleResults

class Comp7BattleInfoSubPresenter(BattleInfoSubPresenter):
    @classmethod
    def getViewModelType(cls):
        ...
    def packBattleResults(self, battleResults):
        ...

def isDeserter(reusable):
    ...
