# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/shop_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler as AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE

class MODULE(object):
    UNEQUIP = 'unequip'
    UNLOAD = 'unload'

class ShopCMHandler(AbstractContextMenuHandler, EventSystemEntity):
    _equipmentCD: Any
    _isCanceled: Any
    def __init__(self, cmProxy, ctx=None):
        ...
    def resetSlot(self):
        ...
    def _initFlashValues(self, ctx):
        ...
    def _clearFlashValues(self):
        ...
    def _generateOptions(self, ctx=None):
        ...
