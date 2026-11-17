# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/gui/Scaleform/hints/proxy.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import Event as Event
from gui.Scaleform.genConsts.TUTORIAL_TRIGGER_TYPES import TUTORIAL_TRIGGER_TYPES as TUTORIAL_TRIGGER_TYPES
from gui.app_loader.settings import APP_NAME_SPACE as APP_NAME_SPACE
from gui.shared import g_eventBus as g_eventBus, events as events
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from tutorial.data.events import ClickEvent as ClickEvent, EnabledChangeEvent as EnabledChangeEvent, VisibleChangeEvent as VisibleChangeEvent
from tutorial.doc_loader.sub_parsers import ACTION_TAGS as ACTION_TAGS
from tutorial.gui import GUI_EFFECT_NAME as GUI_EFFECT_NAME
from tutorial.gui.Scaleform import effects_player as effects_player
from tutorial.gui.Scaleform.lobby.proxy import SfLobbyProxy as SfLobbyProxy

class HintsProxy(SfLobbyProxy):
    __eManager: Any
    onHintClicked: Any
    onHintItemFound: Any
    onHintItemLost: Any
    onVisibleChanged: Any
    onEnabledChanged: Any
    onUpdateTutorialHints: Any
    onImportantHintShowing: Any
    onHintShowing: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def showHint(self, props, ignoreOutsideClick=False, silent=False):
        ...
    def hideHint(self, hintID):
        ...
    def __load(self):
        ...
    def __onAppInitialized(self, event):
        ...
    def __onItemFound(self, event):
        ...
    def __onItemLost(self, event):
        ...
    def __onUpdateTutorialHints(self, event):
        ...
    def __onImportantHintShowing(self, event):
        ...
    def __onTriggerActivated(self, event):
        ...
