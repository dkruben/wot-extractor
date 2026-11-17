# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/hangar_selectable_objects/base_selectable_logic.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
from helpers import dependency as dependency
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from .interfaces import ISelectableLogic as ISelectableLogic, ISelectableLogicCallback as ISelectableLogicCallback
_logger: Any

class BaseSelectableLogic(ISelectableLogic):
    __slots__: tuple
    _hangarSpace: Any
    __callbackRef: Any
    def __init__(self):
        ...
    def init(self, callback=None):
        ...
    def fini(self):
        ...
    def _onNotifyCursorOver3dScene(self, isCursorOver3dScene):
        ...
    def _onMouseEnter(self, entity):
        ...
    def _onMouseExit(self, entity):
        ...
    def _onMouseDown(self):
        ...
    def _onMouseUp(self):
        ...
    def _filterEntity(self, entity):
        ...
    def _callbackMethodCall(self, methodName, *args, **kwargs):
        ...
