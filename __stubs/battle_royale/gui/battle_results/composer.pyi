# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/battle_results/composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_results.composer import IBattleResultStatsCtrl as IBattleResultStatsCtrl
from gui.battle_results.components import base as base
from battle_royale.gui.battle_results import templates as templates
from battle_royale.gui.shared import event_dispatcher as event_dispatcher

class BattleRoyaleStatsComposer(IBattleResultStatsCtrl):
    _block: Any
    def __init__(self, _):
        ...
    def clear(self):
        ...
    def setResults(self, results, reusable):
        ...
    def getVO(self):
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...
    @staticmethod
    def onShowResults(arenaUniqueID):
        ...
