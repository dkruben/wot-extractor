# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_hints/newbie_battle_hints_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
from helpers import dependency as dependency
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.settings_core.settings_constants import GAME as GAME
from debug_utils import LOG_WARNING as LOG_WARNING
from data_structures import VariableState as VariableState
from hints_common.battle.schemas.newbie import configSchema as configSchema
from hints.battle import manager as battleHintsModelsMgr
from hints.battle.newbie import getLogger as getLogger
from hints.battle.schemas.newbie import NewbieClientHintModel as NewbieClientHintModel, hintSchema as hintSchema
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore, ISettingsCache as ISettingsCache
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.battle_hints.newbie_battle_hints_controller import INewbieBattleHintsController as INewbieBattleHintsController
from skeletons.gui.shared import IItemsCache as IItemsCache
from wotdecorators import condition as condition
from uilogging.newbie_hints.loggers import NewbieHintsShownUILogger as NewbieHintsShownUILogger
from hints_common.battle.manager import CommonBattleHintsModelsManager as CommonBattleHintsModelsManager
from hints.battle.schemas.base import CHMType as CHMType
from gui.battle_control.controllers.battle_hints.queues import BattleHint as BattleHint
_PREFS_NAME = 'battleHintsDisplayHistory'
_MISSING: Any
_LOCKED: Any
_COMPLETED = None
NEWBIE_SETTINGS_MAX_BATTLES = 50
NEWBIE_HISTORY_MAX_BATTLES = 200
_ctrlLogger: Any
_historyLogger: Any

class NewbieBattleHintsHistory(object):
    __slots__: tuple
    _itemsCache: Any
    _connectionMgr: Any
    ifEnabled: Any
    _history: Any
    _battlesCount: Any
    _updated: Any
    _enabled: Any
    def __init__(self):
        ...
    # decorador original: @ifEnabled
    def getDisplayCount(self, uniqueName):
        ...
    # decorador original: @ifEnabled
    def reset(self):
        ...
    def destroy(self):
        ...
    # decorador original: @ifEnabled
    def _load(self):
        ...
    def _create(self):
        ...
    def _close(self):
        ...
    def _update(self, battleHint):
        ...
    def _onItemsCacheUpdated(self, *args, **kwargs):
        ...
    def _onDisconnected(self, *args, **kwargs):
        ...
    @staticmethod
    def _isCompleted(modelsMgr, history):
        ...

class NewbieBattleHintsController(INewbieBattleHintsController):
    _settings: Any
    _settingsCache: Any
    _history: Any
    _uiLogger: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def isEnabled(self):
        ...
    def isUserSettingEnabled(self):
        ...
    def getDisplayCount(self, uniqueName):
        ...
    def resetHistory(self):
        ...
