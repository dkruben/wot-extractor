# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/battle/frontline_ingame_rank_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frontline.gui.Scaleform.daapi.view.meta.FrontlineInGameRankMeta import FrontlineInGameRankMeta as FrontlineInGameRankMeta
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE as EPIC_BATTLE
from helpers import dependency as dependency
from math_common import decimal_round as decimal_round
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_MAX_IN_GAME_RANK = 5

class FrontlineInGameRankPanel(FrontlineInGameRankMeta):
    sessionProvider: Any
    __rankThresholds: Any
    __currentRank: Any
    __currentExp: Any
    __waitingForLevelUp: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def levelUpAnimationComplete(self):
        ...
    def __setCurrentRank(self):
        ...
    def __getThresholdPercentage(self, expValue):
        ...
    def __getRank(self, progressValue):
        ...
    def __onPlayerXPUpdated(self, exp):
        ...
