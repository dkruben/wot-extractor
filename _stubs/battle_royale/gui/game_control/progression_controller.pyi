# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/game_control/progression_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import lzip as lzip
import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import BR_PROGRESSION_POINTS_SEEN as BR_PROGRESSION_POINTS_SEEN, BR_UI_SECTION as BR_UI_SECTION
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses
from helpers import dependency as dependency
from battle_royale.skeletons.game_controller import IBRProgressionOnTokensController as IBRProgressionOnTokensController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
_logger: Any

class ProgressionOnTokensController(IBRProgressionOnTokensController):
    STORAGE_SECTION_ACC_SETTINGS_KEY = 'exampleStorage'
    PREV_POINTS_ACC_SETTINGS_KEY = 'exampleLastPointsSeen'
    eventsCache: Any
    lobbyContext: Any
    progressionToken = ''
    onProgressPointsUpdated: Any
    onSettingsChanged: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def saveCurPoints(self):
        ...
    def getPrevPoints(self):
        ...
    def getCurPoints(self):
        ...
    def getProgessionPointsData(self):
        ...
    def _getProgressionLevels(self):
        ...
    def _cachePoints(self, curPoints):
        ...
    def _getCachedPoints(self):
        ...
    def __onTokensUpdate(self, diff, _):
        ...

class ProgressionOnConfig(ProgressionOnTokensController):
    settings: Any
    progressionToken: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    @property
    def isEnabled(self):
        ...
    @property
    def isFinished(self):
        ...
    def setSettings(self, settings):
        ...
    def getProgessionPointsData(self):
        ...
    def _getProgressionLevels(self):
        ...
    def getProgressionData(self):
        ...
    def _getStages(self):
        ...
    def _getMaxPoints(self):
        ...

class _QuestInListContainer(object):
    eventsCache: Any
    questsIds: Any
    def __init__(self):
        ...
    def getQuests(self):
        ...
    def setQuestsIds(self, questsIds):
        ...
    def _filterFunc(self, quest):
        ...

class BaseProgressionWithBattleQuests(ProgressionOnConfig):
    ProgressionFilterFuncKey = 'BRFuncKey'
    questContainer: Any
    def __init__(self):
        ...
    def setSettings(self, settings):
        ...
    def getProgressionData(self):
        ...
    def _getQuestContainer(self):
        ...
    def __getBattleQuestData(self):
        ...

class BRQuests(_QuestInListContainer):
    ...

class BRProgressionController(BaseProgressionWithBattleQuests):
    STORAGE_SECTION_ACC_SETTINGS_KEY = BR_UI_SECTION
    PREV_POINTS_ACC_SETTINGS_KEY = BR_PROGRESSION_POINTS_SEEN
    progressionToken = 'img:battle_royale:progression'
    PROGRESSION_QUEST_PREFIX = 'battle_royale:ticket:progression:'
    def _getQuestContainer(self):
        ...
