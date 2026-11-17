# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/backport/backport_pop_over.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
import logging as logging
from frameworks.wulf import ViewSettings as ViewSettings, ViewModel as ViewModel
from gui.impl.gen import R as R
from gui.impl.pub import PopOverViewImpl as PopOverViewImpl
from gui.shared import g_eventBus as g_eventBus
from gui.shared.events import HidePopoverEvent as HidePopoverEvent
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
_logger: Any
_PopOverData: Any

class BackportPopOverContent(PopOverViewImpl):
    __appLoader: Any
    __slots__: tuple
    def __init__(self, popOverData):
        ...
    def _initialize(self, alias, data):
        ...
    def _finalize(self):
        ...
    def __onPopOverDestroy(self, _):
        ...

def createPopOverData(alias, args=None):
    ...
