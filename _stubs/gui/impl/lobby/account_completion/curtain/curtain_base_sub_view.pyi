# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_completion/curtain/curtain_base_sub_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from typing import Type as Type
from Event import Event as Event
from frameworks.wulf import ViewModel as ViewModel, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from frameworks.wulf import PyResAccessor as PyResAccessor

class CurtainBaseSubView(ViewImpl):
    __slots__: tuple
    _LAYOUT_DYN_ACCESSOR = R.invalid
    _VIEW_MODEL_CLASS = ViewModel
    _isActive: Any
    _isHidden: Any
    onWaitingChanged: Any
    _isWaitingVisible: Any
    _waitingMsgResID: Any
    def __init__(self):
        ...
    @property
    def isActive(self):
        ...
    @property
    def isWaitingVisible(self):
        ...
    @property
    def waitingMsgResID(self):
        ...
    @property
    def isHidden(self):
        ...
    def activate(self, *args, **kwargs):
        ...
    def deactivate(self):
        ...
    def hide(self):
        ...
    def reveal(self):
        ...
    def _finalize(self):
        ...
    def _doFinalize(self):
        ...
    def _setWaiting(self, isVisible, msgResID=...):
        ...
