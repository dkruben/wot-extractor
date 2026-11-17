# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/forsell/forsell_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import option as option, CMLabel as CMLabel, ContextMenu as ContextMenu
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared import event_dispatcher as shared_events
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from gui.shared.event_dispatcher import showSellDialog as showSellDialog

class ForSellCMHandler(ContextMenu, EventSystemEntity):
    __sqGen: Any
    _selected: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    def sell(self):
        ...
    # decorador original: @option(...)
    def switchSaleOption(self):
        ...
    def _getOptionCustomData(self, label):
        ...
    def _initFlashValues(self, ctx):
        ...
