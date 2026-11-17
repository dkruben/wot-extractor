# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/managers/cursor_mgr.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import GUI as GUI
import BigWorld as BigWorld
from gui import GUI_CTRL_MODE_FLAG as _CTRL_FLAG
from gui.Scaleform.framework.entities.abstract.CursorManagerMeta import CursorManagerMeta as CursorManagerMeta
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
_logger: Any

class CursorManager(CursorManagerMeta):
    ARROW = 'arrow'
    AUTO = 'auto'
    BUTTON = 'button'
    HAND = 'hand'
    IBEAM = 'ibeam'
    ROTATE = 'rotate'
    RESIZE = 'resize'
    MOVE = 'move'
    DRAG_OPEN = 'dragopen'
    DRAG_CLOSE = 'dragclose'
    __DAAPI_ERROR = 'flashObject is Python Cursor class can`t be None!'
    __savedMCursorPos: Any
    def __init__(self):
        ...
    def attachCursor(self, flags=...):
        ...
    def detachCursor(self):
        ...
    def syncCursor(self, flags=...):
        ...
    def show(self):
        ...
    def hide(self):
        ...
    def setCursorForced(self, cursor):
        ...
    def _populate(self):
        ...
    def __setSFMousePosition(self):
        ...
    def __saveDeviceMousePosition(self, mouseLeft, mouseTop):
        ...
    def __restoreDeviceMousePosition(self):
        ...
    def resetMousePosition(self):
        ...
