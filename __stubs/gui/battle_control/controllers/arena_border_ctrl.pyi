# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/arena_border_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Math as Math
from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.shared import g_eventBus as g_eventBus
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from gui.doc_loaders import GuiColorsLoader as GuiColorsLoader
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from account_helpers.settings_core import settings_constants as settings_constants

class _SHOW_MODE(object):
    SHOW_BY_ALT_PRESS = 0
    SHOW_ALWAYS = 1
    HIDE = 2
    ALWAYS_HIDE = 3

class _DISPLAY_MODE(object):
    TYPE_WALL = 0
    TYPE_DOTTED = 1
    TYPE_HIDE = 2

class ArenaBorderController(IArenaLoadController):
    settingsCore: Any
    __arenaVisitor: Any
    __spaceID: Any
    __showMode: Any
    __drawType: Any
    __color: Any
    def __init__(self):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def spaceLoadCompleted(self):
        ...
    def getControllerID(self):
        ...
    def getDrawType(self):
        ...
    def _applySetting(self, showMode, drawType, color):
        ...
    def __handleShowExtendedInfo(self, event):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __getCurrentColor(self, colorBlind):
        ...

class BattleRoyaleBorderCtrl(ArenaBorderController):
    def _applySetting(self, showMode, _, color):
        ...
