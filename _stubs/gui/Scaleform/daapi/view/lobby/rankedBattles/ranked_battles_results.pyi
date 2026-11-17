# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_results.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import ENABLE_RANKED_ANIMATIONS as ENABLE_RANKED_ANIMATIONS
from gui.Scaleform.daapi.view.meta.RankedBattlesBattleResultsMeta import RankedBattlesBattleResultsMeta as RankedBattlesBattleResultsMeta
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class RankedBattlesResults(RankedBattlesBattleResultsMeta):
    rankedController: Any
    __slots__: tuple
    __rankedResultsVO: Any
    __rankInfo: Any
    __questsProgress: Any
    __showRankedWidget: Any
    __currentRanks: Any
    __currentRankID: Any
    __lastRankID: Any
    __lastMaxRankID: Any
    def __init__(self, ctx=None):
        ...
    def onWidgetUpdate(self):
        ...
    def onClose(self):
        ...
    def animationCheckBoxSelected(self, value):
        ...
    @property
    def rankedWidget(self):
        ...
    def _populate(self):
        ...
    def __updateRankedWidget(self):
        ...
    def __close(self):
        ...
