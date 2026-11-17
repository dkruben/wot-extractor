# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/prebattle_hints/newbie_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
from logging import getLogger as getLogger
import typing as typing
from account_helpers import AccountSettings as AccountSettings
from account_helpers.settings_core.ServerSettingsManager import SETTINGS_SECTIONS as SETTINGS_SECTIONS
from account_helpers.settings_core.settings_constants import GAME as GAME
from gui.shared import g_eventBus as g_eventBus, events as events
from gui.shared.event_dispatcher import showPrebattleHintsConfirmWindow as showPrebattleHintsConfirmWindow
from helpers import dependency as dependency
from hints_common.prebattle.newbie.consts import BATTLES_TYPES as BATTLES_TYPES
from hints_common.prebattle.newbie.schemas import NewbieHintModel as NewbieHintModel, hintSchema as hintSchema, configSchema as configSchema
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore, ISettingsCache as ISettingsCache
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.prebattle_hints.controller import IPrebattleHintsController as IPrebattleHintsController
from skeletons.gui.prebattle_hints.newbie_controller import INewbiePrebattleHintsController as INewbiePrebattleHintsController
from skeletons.gui.shared import IItemsCache as IItemsCache
from hints_common.prebattle.schemas import BaseHintModel as BaseHintModel
IS_NEWBIE_MAX_BATTLES = 10
_PREFS_NAME = 'prebattle'
_PREFS_DISPLAY_COUNT = 'display_count'
_PREFS_CONFIRMATION = 'confirmation'
_COMPLETED_DISPLAY_COUNT = -1
_DISABLE_HISTORY_THRESHOLD = 50
_logger: Any

class NewbiePrebattleHintsController(INewbiePrebattleHintsController):
    __hintsCtrl: Any
    __settings: Any
    __settingsCache: Any
    __itemsCache: Any
    __connMgr: Any
    __battlesCount: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def hasHintToShow(self, _):
        ...
    def getHintToShow(self, _):
        ...
    def onShowHintsWindowSuccess(self, hint):
        ...
    def onConfirmationWindowShown(self):
        ...
    def isEnabled(self):
        ...
    def __isUserSettingEnabled(self):
        ...
    def __setDefaultPrefs(self):
        ...
    def __onLobbyInited(self, _):
        ...
    def __onItemsCacheSynced(self, *_, **__):
        ...
    def __onDisconnected(self):
        ...
