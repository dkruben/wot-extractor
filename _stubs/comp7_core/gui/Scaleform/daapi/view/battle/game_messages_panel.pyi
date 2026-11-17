# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/game_messages_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.battle_control import avatar_getter as avatar_getter
from helpers import dependency as dependency
from gui.Scaleform.daapi.view.battle.shared.game_messages_panel import GameMessagesPanel as GameMessagesPanel
from gui.impl import backport as backport
from gui.impl.gen import R as R
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from comp7_core_constants import FINISH_REASON as FINISH_REASON

class Comp7GameMessagesPanel(GameMessagesPanel):
    guiSessionProvider: Any
    def sendEndGameMessage(self, winningTeam, reason):
        ...
