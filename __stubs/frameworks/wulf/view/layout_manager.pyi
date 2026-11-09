# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/frameworks/wulf/view/layout_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import defaultdict as defaultdict
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from ..py_object_binder import PyObjectEntity as PyObjectEntity
from typing import Dict as Dict
_logger: Any

class LayoutManager(PyObjectEntity):
    __layouts: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def create(cls, proxy):
        ...
    def createAbsoluteLayout(self, appNS, layoutName):
        ...
    def getLayoutByName(self, appNS, layoutName):
        ...
    def destroyLayouts(self, appNS):
        ...
    def destroy(self):
        ...
