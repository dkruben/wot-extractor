# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/player_stats_in_battle.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.Scaleform.daapi.view.meta.BattleRoyalePlayerStatsMeta import BattleRoyalePlayerStatsMeta as BattleRoyalePlayerStatsMeta
from gui.Scaleform.locale.BATTLE_ROYALE import BATTLE_ROYALE as BATTLE_ROYALE
from gui.battle_control import avatar_getter as avatar_getter
from gui.server_events.battle_royale_formatters import IngameBattleRoyaleResultsViewDataFormatter as IngameBattleRoyaleResultsViewDataFormatter
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController
_logger: Any

class BattleRoyalePlayerStats(BattleRoyalePlayerStatsMeta):
    __sessionProvider: Any
    __battleRoyaleController: Any
    __isInSquad: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _destroy(self):
        ...
    def __onHideDeathScreen(self):
        ...
    def __onShowDeathScreen(self):
        ...
    def __setStpCoins(self):
        ...
