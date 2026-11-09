# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_results/stats_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from frameworks.wulf import ViewModel as ViewModel
from gui.battle_results.reusable import _ReusableInfo as _ReusableInfo
BattleResultsModelType: Any
TooltipModelType: Any
BattleResults: Any

class IBattleResultStatsCtrl(object):
    CTRL_IMPL_TYPE_GAMEFACE = 0
    CTRL_IMPL_TYPE_FLASH = 1
    def clear(self):
        ...
    @property
    def ctrlImplType(self):
        ...
    def setResults(self, results, reusable):
        ...
    def getResults(self):
        ...
    def getVO(self):
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...
    @staticmethod
    def onShowResults(arenaUniqueID):
        ...
    @classmethod
    def representativeArenaBonusType(cls):
        ...
