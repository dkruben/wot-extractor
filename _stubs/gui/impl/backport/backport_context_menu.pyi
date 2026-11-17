# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/backport/backport_context_menu.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from frameworks.wulf import Window as Window, WindowSettings as WindowSettings, WindowFlags as WindowFlags
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
_logger: Any
_ContextMenuData: Any

class BackportContextMenuWindow(Window):
    __appLoader: Any
    __slots__: tuple
    __contextMenuData: Any
    def __init__(self, contextMenuData, parent):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def __contextMenuHideHandler(self):
        ...

def createContextMenuData(contextMenuType, args=None):
    ...
