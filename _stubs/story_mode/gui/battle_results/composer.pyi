# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/battle_results/composer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from logging import getLogger as getLogger
import BigWorld as BigWorld
from gui.battle_results.stats_ctrl import IBattleResultStatsCtrl as IBattleResultStatsCtrl
from gui.battle_results.settings import PLAYER_TEAM_RESULT as PLAYER_TEAM_RESULT
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from story_mode.gui.battle_results.templates import STORY_MODE_RESULTS_BLOCK as STORY_MODE_RESULTS_BLOCK
from story_mode.gui.shared.event_dispatcher import showEpilogueWindow as showEpilogueWindow, showOnboardingBattleResultWindow as showOnboardingBattleResultWindow, showPrebattleAndGoToQueue as showPrebattleAndGoToQueue, showBattleResultWindow as showBattleResultWindow, showOutroVideo as showOutroVideo
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode_common.story_mode_constants import LOGGER_NAME as LOGGER_NAME
_logger: Any

class StoryModeStatsComposer(IBattleResultStatsCtrl):
    _storyModeCtrl: Any
    _lobbyContext: Any
    _block: Any
    def __init__(self, _):
        ...
    def clear(self):
        ...
    def setResults(self, results, reusable):
        ...
    def getVO(self):
        ...
    def onResultsPosted(self, arenaUniqueID):
        ...
    @staticmethod
    def onShowResults(arenaUniqueID):
        ...
    def _processOnboardingResults(self, resultVO):
        ...
