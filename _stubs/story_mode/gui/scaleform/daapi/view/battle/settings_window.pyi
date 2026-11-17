# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/settings_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.settings_core.settings_constants import SETTINGS_GROUP as SETTINGS_GROUP
from gui.Scaleform.daapi.view.common.settings import SettingsWindow as SettingsWindow
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import SettingsTabIndex as SettingsTabIndex
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from story_mode.uilogging.story_mode.consts import LogWindows as LogWindows, LogButtons as LogButtons
from story_mode.uilogging.story_mode.loggers import WindowLogger as WindowLogger

class OnboardingSettingsWindow(SettingsWindow):
    sessionProvider: Any
    _TAB_NAME_TO_INDEX: dict
    _uiLogger: Any
    def __init__(self, **kwargs):
        ...
    def as_setCountersDataS(self, countersData):
        ...
    def applySettings(self, settings, isCloseWnd):
        ...
    def onTabSelected(self, tabId):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
