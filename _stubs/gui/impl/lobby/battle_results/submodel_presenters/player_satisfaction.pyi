# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/submodel_presenters/player_satisfaction.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import logging as logging
from helpers import dependency as dependency
from gui.impl.gui_decorators import args2params as args2params
from gui.battle_results.presenters.battle_results_sub_presenter import BattleResultsSubPresenter as BattleResultsSubPresenter
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from gui.impl.gen.view_models.views.lobby.battle_results.player_satisfaction_model import PlayerSatisfactionModel as PlayerSatisfactionModel, PlayerSatisfactionStates as PlayerSatisfactionStates
from constants import PlayerSatisfactionRating as RatingEnum
from player_satisfaction_schema import playerSatisfactionSchema as playerSatisfactionSchema
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from frameworks.wulf import ViewModel as ViewModel
from typing import Type as Type
from gui.battle_results.stats_ctrl import BattleResults as BattleResults
_logger: Any
_RATING_TO_CHOICE_MAP: dict
_CHOICE_TO_RATING_MAP: dict

class PlayerSatisfactionSubPresenter(BattleResultsSubPresenter):
    __battleResults: Any
    @property
    def arenaUniqueId(self):
        ...
    @property
    def viewModel(self):
        ...
    @classmethod
    def getViewModelType(cls):
        ...
    def _getEvents(self):
        ...
    def packBattleResults(self, battleResults):
        ...
    # decorador original: @args2params(...)
    def selectedChoice(self, state):
        ...
