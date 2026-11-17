# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/ingame_help.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Keys as Keys
from account_helpers.settings_core.settings_constants import CONTROLS as CONTROLS
from gui.Scaleform.daapi.view.meta.IngameDetailsHelpWindowMeta import IngameDetailsHelpWindowMeta as IngameDetailsHelpWindowMeta
from gui.Scaleform.daapi.view.meta.IngameHelpWindowMeta import IngameHelpWindowMeta as IngameHelpWindowMeta
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.Scaleform.genConsts.KEYBOARD_KEYS import KEYBOARD_KEYS as KEYBOARD_KEYS
from gui.Scaleform.managers.battle_input import BattleGUIKeyHandler as BattleGUIKeyHandler
from gui.ingame_help import detailed_help_pages as detailed_help_pages
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.utils.key_mapping import getScaleformKey as getScaleformKey
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_CHANGED_KEYS_IN_HELP: tuple
_FIXED_KEYS_IN_HELP: tuple

class IngameHelpWindow(IngameHelpWindowMeta, BattleGUIKeyHandler):
    settingsCore: Any
    sessionProvider: Any
    def onWindowClose(self):
        ...
    def onWindowMinimize(self):
        ...
    def handleEscKey(self, isDown):
        ...
    def clickSettingWindow(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...

class IngameDetailsHelpWindow(IngameDetailsHelpWindowMeta, BattleGUIKeyHandler):
    sessionProvider: Any
    __ctx: Any
    __detailedList: Any
    def __init__(self, ctx=None):
        ...
    def onWindowClose(self):
        ...
    def onWindowMinimize(self):
        ...
    def handleEscKey(self, isDown):
        ...
    def _populate(self):
        ...
    def requestPageData(self, index):
        ...
    def _dispose(self):
        ...

def getChangedKeysInfo(settingsCore):
    ...
def getFixedKeysInfo():
    ...
