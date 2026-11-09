# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/managers/PopoverManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.framework.entities.abstract.PopoverManagerMeta import PopoverManagerMeta as PopoverManagerMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.shared.events import HidePopoverEvent as HidePopoverEvent

class PopoverManager(PopoverManagerMeta):
    __scope: Any
    def __init__(self, scope):
        ...
    def requestShowPopover(self, alias, data):
        ...
    def requestHidePopover(self):
        ...
    def destroy(self):
        ...
    def __handlerDestroyPopover(self, _):
        ...
