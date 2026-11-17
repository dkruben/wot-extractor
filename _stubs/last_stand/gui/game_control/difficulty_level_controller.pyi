# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/gui/game_control/difficulty_level_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
import typing as typing
from collections import namedtuple as namedtuple
from Event import Event as Event, EventManager as EventManager
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from last_stand.gui.ls_gui_constants import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from last_stand.gui import ls_account_settings as ls_account_settings
from last_stand.gui.ls_gui_constants import DifficultyLevel as DifficultyLevel, QUEUE_TYPE_TO_DIFFICULTY_LEVEL as QUEUE_TYPE_TO_DIFFICULTY_LEVEL
from last_stand.gui.ls_account_settings import AccountSettingsKeys as AccountSettingsKeys, getFirstNewStatusUnlockLevel as getFirstNewStatusUnlockLevel
from last_stand.gui.prb_control.entities.squad.entity import LastStandSquadEntity as LastStandSquadEntity
from last_stand.skeletons.difficulty_level_controller import IDifficultyLevelController as IDifficultyLevelController
from last_stand.skeletons.ls_controller import ILSController as ILSController
from last_stand_common.last_stand_constants import LAST_STAND_QUEUE_TYPES as LAST_STAND_QUEUE_TYPES, QUEUE_TYPE as QUEUE_TYPE, DifficultyLevelToken as DifficultyLevelToken, TOKEN_DIFFICULTY_LEVEL_TO_QUEUE_TYPE as TOKEN_DIFFICULTY_LEVEL_TO_QUEUE_TYPE
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from helpers import dependency as dependency
from shared_utils import findFirst as findFirst
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.prb_control.entities.base.entity import BasePrbEntity as BasePrbEntity
_Level: Any

class DifficultyLevelController(IDifficultyLevelController, IGlobalListener):
    _itemsCache: Any
    lsCtrl: Any
    _em: Any
    onChangeDifficultyLevelStatus: Any
    onChangeDifficultyLevel: Any
    onLevelsInfoReady: Any
    selectedLevel: Any
    items: Any
    def __init__(self):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def onPrbEntitySwitched(self):
        ...
    def onDequeued(self, queueType, *args):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def getLastSelectedLevel(self):
        ...
    def getLevelsInfo(self):
        ...
    def getLevelInfo(self, levelNum):
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
