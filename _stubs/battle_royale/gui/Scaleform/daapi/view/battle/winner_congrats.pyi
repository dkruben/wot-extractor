# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/winner_congrats.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from battle_royale.gui.battle_control.controllers.br_battle_sounds import BREvents as BREvents
from gui.Scaleform.daapi.view.meta.BattleRoyaleWinnerCongratsMeta import BattleRoyaleWinnerCongratsMeta as BattleRoyaleWinnerCongratsMeta
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class BattleRoyaleWinnerCongrats(BattleRoyaleWinnerCongratsMeta):
    __battleRoyaleController: Any
    __sessionProvider: Any
    __winnerStpCoins: Any
    def playWinSound(self):
        ...
    def _populate(self):
        ...
    def _destroy(self):
        ...
    def __onWinnerScreen(self):
        ...
    def __setStpCoins(self):
        ...
