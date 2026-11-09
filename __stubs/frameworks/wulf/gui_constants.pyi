# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/frameworks/wulf/gui_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from shared_utils import CONST_CONTAINER as CONST_CONTAINER

class ViewStatus(CONST_CONTAINER):
    UNDEFINED = 0
    CREATED = 1
    LOADING = 2
    LOADED = 3
    DESTROYING = 4
    DESTROYED = 5

class ShowingStatus(Enum):
    SHOWING = 0
    SHOWN = 1
    HIDING = 2
    HIDDEN = 3

class ViewFlags(CONST_CONTAINER):
    VIEW = 1
    WINDOW_DECORATOR = 2
    POP_OVER_DECORATOR: Any
    MAIN_VIEW = 8
    OLD_STYLE_VIEW = 32
    LOBBY_SUB_VIEW: Any
    LOBBY_TOP_SUB_VIEW: Any
    VIEW_TYPE_MASK = 65520
    @classmethod
    def getViewType(cls, flags):
        ...

class ViewEventType(CONST_CONTAINER):
    UNDEFINED = 0
    TOOLTIP = 1
    POP_OVER = 2
    CONTEXT_MENU = 4
    DROP_DOWN = 8

class WindowStatus(CONST_CONTAINER):
    UNDEFINED = 0
    CREATED = 1
    LOADING = 2
    LOADED = 3
    DESTROYING = 4
    DESTROYED = 5

class WindowFlags(CONST_CONTAINER):
    UNDEFINED = 0
    WINDOW = 1
    GLOBAL_WINDOW = 2
    MAIN_WINDOW: Any
    SURFACE = 8
    DIALOG: Any
    POP_OVER: Any
    TOOLTIP: Any
    CONTEXT_MENU: Any
    DROP_DOWN: Any
    SERVICE_WINDOW: Any
    WAITING: Any
    WINDOW_TYPE_MASK = 255
    WINDOW_MINIMIZED = 256
    WINDOW_MAXIMIZED = 512
    WINDOW_FULLSCREEN = 1024
    WINDOW_STATE_MASK = 3840
    WINDOW_MODAL = 4096
    APP_MODAL = 8192
    WINDOW_MODALITY_MASK = 12288

class WindowLayer(CONST_CONTAINER):
    UNDEFINED = 0
    ROOT = 1
    HIDDEN_SERVICE_LAYOUT = 2
    MARKER = 3
    VIEW = 4
    SUB_VIEW = 5
    TOP_SUB_VIEW = 6
    WINDOW = 7
    FULLSCREEN_WINDOW = 8
    SYSTEM_MESSAGE = 9
    TOP_WINDOW = 10
    OVERLAY = 11
    IME = 12
    SERVICE_LAYOUT = 13
    TOOLTIP = 14
    CURSOR = 15
    WAITING = 16

class PositionAnchor(CONST_CONTAINER):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3

class NumberFormatType(CONST_CONTAINER):
    INTEGRAL = 0
    GOLD = 1

class RealFormatType(CONST_CONTAINER):
    FRACTIONAL = 0
    WO_ZERO_DIGITS = 1

class TimeFormatType(CONST_CONTAINER):
    SHORT_FORMAT = 0
    LONG_FORMAT = 1

class DateFormatType(CONST_CONTAINER):
    SHORT_FORMAT = 0
    LONG_FORMAT = 1
    YEAR_MONTH = 2

class CaseType(CONST_CONTAINER):
    UPPERCASE = 0
    LOWERCASE = 1

class ChildFlags(CONST_CONTAINER):
    EMPTY = 0
    AUTO_DESTROY = 1
