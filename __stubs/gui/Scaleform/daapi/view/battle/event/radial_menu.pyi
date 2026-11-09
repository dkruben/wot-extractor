# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/event/radial_menu.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from gui.Scaleform.daapi.view.battle.shared.radial_menu import RadialMenu as RadialMenu
from gui.battle_control.controllers.chat_cmd_ctrl import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES
from gui.Scaleform.managers.cursor_mgr import CursorManager as CursorManager
from gui.Scaleform.daapi.view.meta.EventRadialMenuMeta import EventRadialMenuMeta as EventRadialMenuMeta
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
EventShortcut: Any
_CMD_LOCALE_PFX = '#ingame_help:chatShortcuts/'
SHORTCUTS_EVENT: tuple
PAGE_DEFAULT: tuple
PAGE_ALLY: tuple
PAGE_ENEMY: tuple
PAGE_CHAT_DEFAULT: tuple
PAGE_CHAT_ALLY: tuple
SHORTCUT_BY_ACTION: dict

class EventRadialMenu(RadialMenu, EventRadialMenuMeta):
    def onAction(self, action):
        ...
    def showHandCursor(self):
        ...
    def hideHandCursor(self):
        ...
    def leaveRadialMode(self):
        ...
    def hide(self, allowAction=True):
        ...
    def _showInternal(self, radialState, offset, ratio):
        ...
    def _getTargetDisplayName(self):
        ...

def __makeShortcutSet(commands):
    ...
