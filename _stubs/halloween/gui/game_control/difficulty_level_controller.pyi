# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/game_control/difficulty_level_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
from future.utils import viewvalues as viewvalues
from Event import Event as Event, EventManager as EventManager
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from halloween.gui import halloween_account_settings as halloween_account_settings
from halloween.gui.halloween_gui_constants import DifficultyLevel as DifficultyLevel, QUEUE_TYPE_TO_DIFFICULTY_LEVEL as QUEUE_TYPE_TO_DIFFICULTY_LEVEL
from halloween.gui.halloween_account_settings import AccountSettingsKeys as AccountSettingsKeys
from halloween.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween_common.halloween_constants import QUEUE_TYPE as QUEUE_TYPE, DifficultyLevelToken as DifficultyLevelToken, TOKEN_DIFFICULTY_LEVEL_TO_QUEUE_TYPE as TOKEN_DIFFICULTY_LEVEL_TO_QUEUE_TYPE
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.shared import IItemsCache as IItemsCache
_Level: Any

class DifficultyLevelController(IDifficultyLevelController):
    _itemsCache: Any
    __halloweenBattleCtrl: Any
    _em: Any
    onChangeDifficultyLevelStatus: Any
    onChangeDifficultyLevel: Any
    selectedLevel: Any
    items: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    @staticmethod
    def getLastSelectedLevel():
        ...
    def getLevelsInfo(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onLobbyStarted(self, ctx):
        ...
    def selectLevel(self, level):
        ...
    def getSelectedLevel(self):
        ...
    def getCurrentQueueType(self):
        ...
    def _onSyncTokensCompleted(self, diff):
        ...
    def _getLevelInfo(self, token):
        ...
    def __setNewStatus(self, level):
        ...
