# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/hints_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import listitems as listitems, viewitems as viewitems, viewkeys as viewkeys
from account_helpers.settings_core.settings_constants import OnceOnlyHints as OnceOnlyHints
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.tutorial import ITutorialLoader as ITutorialLoader
from tutorial import settings as settings
from tutorial.control.context import GlobalStorage as GlobalStorage
from tutorial.control.functional import FunctionalConditions as FunctionalConditions
from tutorial.data.client_triggers import ClientTriggers as ClientTriggers
from tutorial.data.hints import HintProps as HintProps
from tutorial.doc_loader.parsers import HintsParser as HintsParser
from tutorial.gui.Scaleform.hints.proxy import HintsProxy as HintsProxy
_logger: Any
HINT_SHOWN_STATUS = 1
_MAX_ACTIVE_HINTS = 1
_DESCRIPTOR_PATH: Any

class HintsManager(object):
    __settingsCore: Any
    __tutorialLoader: Any
    __slots__: tuple
    _data: Any
    _gui: Any
    __activeHints: Any
    __postponedHints: Any
    __hintsWithClientTriggers: Any
    def __init__(self):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def __loadHintsData(self):
        ...
    def __setTriggeredComponents(self):
        ...
    def __showHint(self, hint, silent=False):
        ...
    def __hideHint(self, itemID, hintID=''):
        ...
    def __onGUILoaded(self):
        ...
    def __onGUIInput(self, event):
        ...
    def __onItemFound(self, itemID, silent=False):
        ...
    def __onItemLost(self, itemID):
        ...
    def __onItemVisibleChanged(self, event):
        ...
    def __onItemEnabledChanged(self, event):
        ...
    def __updateItemState(self, event):
        ...
    def __getActiveHintIdByItemId(self, itemID):
        ...
    def __stopOnceOnlyHint(self, itemID, hintID):
        ...
    @staticmethod
    def __checkConditions(hint):
        ...
    def __startSettingsListening(self):
        ...
    def __stopSettingsListening(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __onGlobalConditionValueChanged(self, conditionId, value):
        ...
    def __onUpdateTutorialHints(self, conditionId, state, arguments=''):
        ...
    @staticmethod
    def __filterConditions(conditions, filterFunction, *args):
        ...
    def __onImportantHintShowing(self, state):
        ...
    def __tryPushPostponed(self):
        ...
    @staticmethod
    def __filterByLimitedUIRule(condition, conditionId, arguments=''):
        ...
    @staticmethod
    def __filterByConditionId(condition, conditionId):
        ...
