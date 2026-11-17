# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/scaleform/daapi/view/battle/game_messages_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import FINISH_REASON as FINISH_REASON
from gui.Scaleform.daapi.view.battle.shared.game_messages_panel import GameMessagesPanel as GameMessagesPanel, PlayerMessageData as PlayerMessageData
from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS as GAME_MESSAGES_CONSTS
from gui.battle_control import avatar_getter as avatar_getter
from gui.impl import backport as backport
from gui.impl.gen import R as R

class FortRushGameMessagesPanel(GameMessagesPanel):
    def sendEndGameMessage(self, winningTeam, reason):
        ...
