# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/personalreserves/boosters_cm_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from gui import shop as shop
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import ContextMenu as ContextMenu, option as option, CMLabel as CMLabel
from gui.Scaleform.framework.managers.context_menu import CM_BUY_COLOR as CM_BUY_COLOR
from gui.shared import event_dispatcher as shared_events
from helpers import dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
_SOURCE = shop.Source.EXTERNAL
_ORIGIN = shop.Origin.STORAGE

class PersonalReservesCMHandler(ContextMenu):
    __sqGen: Any
    __goodiesCache: Any
    # decorador original: @option(...)
    def showInfo(self):
        ...
    # decorador original: @option(...)
    # decorador original: @adisp_process
    def activate(self):
        ...
    # decorador original: @option(...)
    def buy(self):
        ...
    def _getOptionCustomData(self, label):
        ...
