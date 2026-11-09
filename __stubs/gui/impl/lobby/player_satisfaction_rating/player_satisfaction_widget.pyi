# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/player_satisfaction_rating/player_satisfaction_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from constants import PlayerSatisfactionRating as RatingEnum
from gui.Scaleform.daapi.view.meta.PlayerSatisfactionWidgetMeta import PlayerSatisfactionWidgetMeta as PlayerSatisfactionWidgetMeta
from gui.Scaleform.genConsts.PLAYER_SATISFACTION_RATING import PLAYER_SATISFACTION_RATING as PLAYER_SATISFACTION_RATING
from gui.Scaleform.daapi.view.battle_results_window import IBattleResultsComponent as IBattleResultsComponent
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
_logger: Any
_RATING_TO_CHOICE_MAP: dict
_CHOICE_TO_RATING_MAP: dict

class PlayerSatisfactionWidget(PlayerSatisfactionWidgetMeta, IBattleResultsComponent):
    __battleResults: Any
    _arenaUniqueID: Any
    def __init__(self):
        ...
    def setArenaUniqueID(self, arenaUniqueID):
        ...
    def selectedChoice(self, choice):
        ...
