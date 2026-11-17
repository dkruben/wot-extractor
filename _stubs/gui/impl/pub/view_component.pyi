# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/view_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import weakref as weakref
from future.utils import iteritems as iteritems
from typing import TYPE_CHECKING as TYPE_CHECKING
from Event import Event as Event, EventManager as EventManager
from frameworks.wulf import ViewModel as ViewModel, ViewSettings as ViewSettings, ViewStatus as ViewStatus
from frameworks.wulf.gui_constants import ChildFlags as ChildFlags
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.view_impl import TViewModel as TViewModel
from typing import Any as Any, Callable as Callable, Dict as Dict, Optional as Optional, Type as Type, Tuple as Tuple, Union as Union, Set as Set
from _weakref import ReferenceType as ReferenceType
_logger: _Any

# base nao representavel no stub: ViewImpl[...]
class ViewComponent:
    __enabled: _Any
    _childrenByUid: _Any
    _childrenUidByPosition: _Any
    _childPositionByUid: _Any
    __childrenInited: _Any
    __em: _Any
    onEnabledChanged: _Any
    _root: _Any
    __dependents: _Any
    __dependencies: _Any
    def __init__(self, layoutID=..., model=..., enabled=True, sharedLayoutId=0, *args, **kwargs):
        ...
    @property
    def dependents(self):
        ...
    @property
    def dependencies(self):
        ...
    def prepare(self):
        ...
    def isEnabled(self):
        ...
    def getChildByPosId(self, posId):
        ...
    def setEnabled(self, value):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getChildComponents(self):
        ...
    def _initChildren(self):
        ...
    def _constructChild(self, posId, viewFactory=None):
        ...
    def _registerChild(self, posId, child):
        ...
    def _prepareChildren(self):
        ...
    def _getRoot(self):
        ...
    def _setChild(self, posId, child):
        ...
    def _getChild(self, posId):
        ...
    def _prepareChild(self, uid, child):
        ...
    def _finalize(self):
        ...
    def _unregisterChild(self, uid, destroy):
        ...
    def _removeChildren(self):
        ...
    def __constructChildFromFactory(self, resId, *args, **kwargs):
        ...
    def __onChildEnabledChanged(self, uid):
        ...
