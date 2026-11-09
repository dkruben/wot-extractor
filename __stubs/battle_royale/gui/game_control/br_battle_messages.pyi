# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/game_control/br_battle_messages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency, int2roman as int2roman
from battle_royale.gui.battle_control.controllers.progression_ctrl import IProgressionListener as IProgressionListener
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
import BattleReplay as BattleReplay

class ProgressionMessagesPlayer(IProgressionListener):
    _sessionProvider: Any
    def updateData(self, arenaLevelData):
        ...
    def onMaxLvlAchieved(self):
        ...
