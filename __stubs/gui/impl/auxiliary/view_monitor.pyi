# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/auxiliary/view_monitor.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
import logging as logging
import weakref as weakref
from frameworks.wulf import ViewStatus as ViewStatus
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from typing import Optional as Optional, Set as Set, Iterable as Iterable
_logger: Any

class ViewMonitor(object):
    __slots__: tuple
    __gui: Any
    _view: Any
    _ignoreViewLayoutIds: Any
    def __init__(self):
        ...
    def init(self, view, ignoreViewLayoutIds=None):
        ...
    def fini(self):
        ...
    def __viewStatusChanged(self, viewUniqueID, viewNewStatus):
        ...
