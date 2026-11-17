# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/presenters/packers/battle_info.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.battle_results.pbs_helpers.common import getArenaNameStr as getArenaNameStr, getRegularFinishResultResource as getRegularFinishResultResource
from gui.battle_results.presenters.packers.interfaces import IBattleResultsPacker as IBattleResultsPacker
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD

class BattleInfo(IBattleResultsPacker):
    @classmethod
    def packModel(cls, model, battleResults):
        ...
    @classmethod
    def _packTeamResult(cls, model, reusable, results):
        ...
    @classmethod
    def _getFinishReasonResource(cls, reusable, results):
        ...
    @classmethod
    def _getWinStatus(cls, reusable, results):
        ...
