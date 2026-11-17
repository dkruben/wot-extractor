# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/messengerBar/ChannelListContextMenuHandler.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler as AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ChannelCarouselEvent as ChannelCarouselEvent

class CHANNEL(object):
    CLOSE_CURRENT = 'closeCurrent'
    MINIMIZE_ALL = 'minimizeAll'
    CLOSE_ALL_EXCEPT_CURRENT = 'closeAllExceptCurrent'

class ChannelListContextMenuHandler(AbstractContextMenuHandler, EventSystemEntity):
    _clientID: Any
    _canClose: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def closeCurrent(self):
        ...
    def minimizeAll(self):
        ...
    def closeAllExceptCurrent(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
